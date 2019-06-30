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

from instructions.Comment import Comment
from instructions.EndProgram import EndProgram
from statements.Empty import Empty
from statements.Declaration import Declaration
from statements.Function import Function
from statements.FunctionCall import FunctionCall
from statements.Identifier import Identifier
from statements.MyAssignment import MyAssignment
from statements.MyConstant import MyConstant


class Compiler:
    def __init__(self, code):
        self.code = code
        self.global_variables = set()
        self.structs = set()
        self.functions = []
        self.instructions = []
        self.global_environment = True  # variable indicating whether the instruction is in the global environment or local environment, i.e. in a function

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
            assignment.add_to_body(right.get_instructions())
            assignment.add_to_body(left.get_instructions())
            return assignment

        # Declaration
        elif isinstance(e, Decl):
            if isinstance(e.type, TypeDecl):
                declaration = Declaration(e.name, 'int', 1, self.global_environment, 'register' in e.storage)

                init_value = e.init
                if init_value is not None:
                    s = self.build_type(init_value)
                    declaration.add_to_body(s.get_instructions())

                if declaration.is_global_variable():
                    self.global_variables.add(declaration)
                    return Empty()
                else:
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
            for b in e.body.block_items:
                s = self.build_type(b)
                function.add_to_body(s.get_instructions())  # TODO: Local variable declarations must be restored

            # self.functions.append(function)
            self.global_environment = True
            return function

        # Identifier
        elif isinstance(e, ID):
            return Identifier(e.name)

        # Function call
        elif isinstance(e, FuncCall):
            function_call = FunctionCall(e.name.name, e.attr_names)
            return function_call

        # While loop
        elif isinstance(e, While):
            pass

        elif isinstance(e, Constant):
            return MyConstant(e.value)

        # Error
        else:
            raise Exception("Unknown statement or expression: " + str(type(e)))

    def build(self):
        # Functions
        for function in self.functions:
            for instruction in function.get_instructions():
                self.instructions.append(instruction)

        # Global variables
        self.instructions.append(Comment("Global variables"))
        self.instructions.append(Comment("----------------"))
        for global_variable in self.global_variables:
            self.instructions.extend(global_variable.get_instructions())

        # Program termination
        self.instructions.append(EndProgram())

        assembly = ''
        for instruction in self.instructions:
            assembly += str(instruction)
            assembly += '\n'
        return assembly
