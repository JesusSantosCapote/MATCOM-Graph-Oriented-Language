from enum import Enum

class DataType(Enum):
    INT = 1
    FLOAT = 2
    STRING = 3
    GRAPH = 4
    DIGRAPH = 5
    PSEUDOGRAPH = 6


class Symbol():
    def __init__(self, id, data_type, value) :
        self.id = id
        self.data_type = data_type
        self.value = value
    def __str__(self):
        string = f"{self.id} {self.data_type} {self.value}"
        return string


class SymbolTable():
    def __init__(self, symbols = {}) :
        self.symbols = symbols


    def add(self, symbol):
        self.symbols[symbol.id] = symbol
    

    def get(self, id):
        if not id in self.symbols:
            raise Exception('Error: variable ', id, ' not defined.')

        return self.symbols[id]


    def update(self, symbol) :
        if not symbol.id in self.symbols :
            raise Exception('Error: variable ', symbol.id, ' not defined.')
        else :
            self.symbols[symbol.id] = symbol

    def Clone(self) :
        return SymbolTable(self.symbols.copy())