#-----------------------------------------------------------------
# pycparser: serialize_ast.py
#
# Simple example of serializing AST
#
# Hart Chu [https://github.com/CtheSky]
# Eli Bendersky [https://eli.thegreenplace.net/]
# License: BSD
#-----------------------------------------------------------------
from __future__ import print_function
import pickle

from pycparser import c_parser
from pycparser.c_ast import *

from ActivationRecord import ActivationRecord
from MemoryAllocation import MemoryAllocation
from expressions.MyBinaryOperation import MyBinaryOperation
from instructions.Comment import Comment
from instructions.EmptyLine import EmptyLine
from instructions.EndProgram import EndProgram
from statements.Empty import Empty
from statements.Declaration import Declaration
from statements.Function import Function
from statements.FunctionCall import FunctionCall
from statements.Identifier import Identifier
from statements.MyAssignment import MyAssignment
from statements.MyConstant import MyConstant
from statements.MyIf import MyIf
from statements.MyWhile import MyWhile


class Compiler:
    def __init__(self, code):
        self.code = code
        self.global_variables = dict()
        self.structs = set()
        self.functions = dict()
        self.activation_records = set()
        self.instructions = []
        self.memory_allocation = MemoryAllocation()
        self.global_environment = True  # variable indicating whether the instruction is in the global environment or local environment, i.e. in a function
        self.function_environment = None
        self.move_to_register = False

    def parse(self):
        parser = c_parser.CParser()
        ast = parser.parse(self.code)

        # Since AST nodes use __slots__ for faster attribute access and
        # space saving, it needs Pickle's protocol version >= 2.
        # The default version is 3 for python 3.x and 1 for python 2.7.
        # You can always select the highest available protocol with the -1 argument.
        with open('ast', 'wb') as f:
            pickle.dump(ast, f, protocol=-1)

    def compile(self):
        with open('ast', 'rb') as f:
            ast = pickle.load(f)
            ast.show()
            for e in ast.ext:
                print(type(e))
                s = self.build_type(e)
                self.instructions.extend(s.get_instructions())

    def build_type(self, e):

        # Assignment
        if isinstance(e, Assignment):
            left = self.build_type(e.lvalue)
            right = self.build_type(e.rvalue)
            assignment = MyAssignment(left, right)
            assignment.add_to_body(right.get_instructions(self.function_environment, self.memory_allocation))
            assignment.add_to_body(left.get_instructions(self.function_environment, self.memory_allocation))
            # assignment.get_instructions(self.function_environment, self.memory_allocation)
            return assignment

        # Declaration
        elif isinstance(e, Decl):
            if isinstance(e.type, TypeDecl):
                declaration = Declaration(e.name, 'int', 1, self.global_environment, 'register' in e.storage)

                self.memory_allocation.allocate(declaration, self.function_environment)

                init_value = e.init
                if init_value is not None:
                    s = self.build_type(init_value)
                    declaration.add_to_body(s.get_instructions(self.function_environment, self.memory_allocation))

                if declaration.is_global_variable():
                    self.global_variables[declaration.name] = declaration
                    return Empty()
                else:
                    # self.function_environment.add_local_variable(declaration)
                    return declaration
            elif isinstance(e.type, ArrayDecl):
                pass
            elif isinstance(e.type, Struct):
                declaration = Struct(e.type.name, e.type.decls)
                return declaration
            else:
                raise Exception("Invalid declaration type.")

        # Function
        elif isinstance(e, FuncDef):
            self.global_environment = False
            function = Function(e.decl.name, e.param_decls)
            self.function_environment = function
            activation_record = ActivationRecord(function)
            self.activation_records.add(activation_record)
            for b in e.body.block_items:
                s = self.build_type(b)
                function.add_to_body(s.get_instructions(function, self.memory_allocation))  # TODO: Local variable declarations must be restored

            self.functions[function.name] = function
            self.global_environment = True
            self.function_environment = None
            return function

        # Identifier
        elif isinstance(e, ID):
            return Identifier(e.name, self.move_to_register)

        # Function call
        elif isinstance(e, FuncCall):
            function_call = FunctionCall(e.name.name, e.attr_names)
            return function_call

        # While loop
        elif isinstance(e, While):
            condition = self.build_type(e.cond)
            my_while = MyWhile(condition, e.stmt)
            for b in e.stmt:
                s = self.build_type(b)
                my_while.add_to_body(s.get_instructions(self.function_environment, self.memory_allocation))
            return my_while

        elif isinstance(e, If):
            condition = self.build_type(e.cond)
            my_if = MyIf(condition, e.iftrue, e.iffalse)
            # for b in e.iftrue:
            #     s = self.build_type(b)
            #     my_if.add_to_body(s.get_instructions(self.function_environment, self.memory_allocation))
            # for b in e.iffalse:
            #     s = self.build_type(b)
            #     my_if.add_to_body(s.get_instructions(self.function_environment, self.memory_allocation))
            return my_if

        elif isinstance(e, BinaryOp):
            my_binary_operation = MyBinaryOperation(e.left, e.right, e.op)
            self.move_to_register = True
            ls = self.build_type(e.left)
            self.move_to_register = False

            self.move_to_register = True
            rs = self.build_type(e.right)
            self.move_to_register = False

            my_binary_operation.add_to_body(ls.get_instructions(self.function_environment, self.memory_allocation))
            my_binary_operation.add_to_body(rs.get_instructions(self.function_environment, self.memory_allocation))
            return my_binary_operation

        elif isinstance(e, Constant):
            return MyConstant(e.value)

        # Error
        else:
            raise Exception("Unknown statement or expression: " + str(type(e)))

    def build(self):
        # Activation records
        self.instructions.append(EmptyLine())
        for activation_record in self.activation_records:
            self.instructions.extend(activation_record.get_instructions(self.memory_allocation))

        self.instructions.append(EmptyLine())

        # Local variables
        for function in self.functions.values():
            head = 'Lokale variabelen ' + function.name
            self.instructions.append(Comment(head))
            self.instructions.append(Comment(''.join('-' for i in range(len(head)))))
            for local_variable in function.get_local_variables():
                self.instructions.append(Comment(local_variable.name + ' -> ' + self.memory_allocation.get_address(local_variable, function)))



        # Functions
        # for function in self.functions.values():
        #     for instruction in function.get_instructions():
        #         self.instructions.append(instruction)

        # Global variables
        self.instructions.append(EmptyLine())
        self.instructions.append(Comment("Globale variablen"))
        self.instructions.append(Comment("-----------------"))
        for global_variable in self.global_variables.values():
            self.instructions.extend(global_variable.get_instructions())

        # Program termination
        self.instructions.append(EndProgram())

        assembly = ''
        for instruction in self.instructions:
            assembly += str(instruction)
            assembly += '\n'
        return assembly
