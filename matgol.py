import sys
from parser_rules import parser
from symbol_table import *
class DSL:

    def main(self, file_name = None):
        if file_name != None:
            self.run_file(file_name)

    def run_file(self, file_name):
        code = ""
        with open(file_name) as file:
            code = file.read()
        file.close()

        self.run(code)
    
    def run(self, source):
        program = parser.parse(source)
        st = SymbolTable()
        program.evaluate(st)
        print(st.symbols)

my_DSL = DSL()
source = f"input_codes/{input()}.txt"
my_DSL.main(source)



