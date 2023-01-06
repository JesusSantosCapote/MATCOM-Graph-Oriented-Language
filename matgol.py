#!/usr/bin/env python3

from optparse import OptionParser
from parser_rules import parser
from symbol_table import SymbolTable


class DSL:
    def main(self, file_name=None):
        if file_name != None:
            self.run_file(file_name)

    def run_file(self, file_name):
        code = ""

        with open(file_name) as file:
            code = file.read()

        self.run(code)

    def run(self, source):
        program = parser.parse(source)
        st = SymbolTable()
        program.evaluate(st)
        print(st.symbols)


if __name__ == "__main__":
    usage = "matgol.py source"
    parser = OptionParser(usage=usage)

    options, args = parser.parse_args()
    if len(args) != 1:
        parser.error("Incorrect number of arguments")

    source = args[0]
    print(source)
    dsl = DSL()
    dsl.main(source)
