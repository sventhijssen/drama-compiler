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
from statements.Declaration import Declaration
from statements.Function import Function
from instructions.Instruction import Instruction


class Compiler:
    def __init__(self, code):
        self.code = code
        self.global_variables = set()
        self.structs = set()
        self.functions = []
        self.instructions = []
        self.global_environment = True # variable indicating whether the instruction is in the global environment or local environment, i.e. in a function


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
                self.build_type(e)

    def build_type(self, e):

        # Assignment
        if isinstance(e, Assignment):
            pass
            # name = self.build_type(e.lvalue)
            # assignment = Assignment(e.lvalue.name, e.rvalue)
            # return assignment

        # Declaration
        elif isinstance(e, Decl):
            if isinstance(e.type, TypeDecl):
                value = None
                if e.init is not None:
                    value = self.build_type(e.init)
                declaration = Declaration(e.name, e.type.type.names[0], value, 1, self.global_environment,
                                          'register' in e.storage)
                if declaration.is_global_variable():
                    self.global_variables.add(declaration)
                declaration
            elif isinstance(e.type, ArrayDecl):
                pass
            elif isinstance(e.type, Struct):
                declaration = Struct(e.type.name, e.type.decls)
                declaration
            else:
                raise ("Invalid declaration type.")

        # Function
        elif isinstance(e, FuncDef):
            self.global_environment = False
            function = Function(e.decl.name, e.param_decls, e.body.block_items)
            for s in e.body.block_items:
                self.build_type(s)
            self.global_environment = True

        # ?
        elif isinstance(e, ID):
            pass

        # Function call
        elif isinstance(e, FuncCall):
            if e.name.name == 'getint':  # getint()
                return Instruction(opcode='LEZ', comment='getint()')
            else:
                pass

        # While loop
        elif isinstance(e, While):
            pass

        elif isinstance(e, Constant):
            return e.value

        # Error
        else:
            raise Exception("Unknown statement or expression: " + str(type(e)))

    def build(self):
        # Functions
        for function in self.functions:
            pass

        # Global variables
        self.instructions.append(Comment("Global variables"))
        self.instructions.append(Comment("----------------"))
        for global_variable in self.global_variables:
            self.instructions.append(global_variable.get_instructions())

        # Program termination
        self.instructions.append(EndProgram())

        assembly = ''
        for instruction in self.instructions:
            assembly += str(instruction)
            assembly += '\n'
        return assembly
