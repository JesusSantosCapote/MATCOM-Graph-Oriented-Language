from abc import ABC, abstractmethod
from symbol_table import *


class Node(ABC):
    @abstractmethod
    def evaluate(self, st):
        pass       


class Instructions(Node):
    def __init__(self, node_list) -> None:
        self.node_list = node_list

    def evaluate(self, st):
        for instruction in self.node_list:
            instruction.evaluate(st)


class Plot(Node) :

    def __init__(self,  graph) :
        self.graph = graph

    def evaluate(self, st): #TODO not implemented
        pass


class Assign(Node) :

    def __init__(self, id, graph_type, vertex, edges_expression) :
        self.id = id
        self.graph_type = graph_type
        self.vertex = vertex
        self.edges_expression = edges_expression

    def evaluate(self, symbol_table : SymbolTable):
        
        for edge in range (len(self.edges_expression)):
            if self.edges_expression[edge][0] >= self.vertex or self.edges_expression[edge][0] < 0 or self.edges_expression[edge][1] >= self.vertex or self.edges_expression[edge][1] < 0:
                raise Exception("Edge non-existent")
            if self.graph_type != "PSEUDOGRAPH":
                if self.edges_expression[edge][0] == self.edges_expression[edge][1]:
                    raise Exception(f"{self.graph_type} can not have loop edges")
            if self.graph_type != "MULTIGRAPH":
                for remain_edge in range(edge + 1, len(self.edges_expression)):
                    if self.edges_expression[remain_edge][0] == self.edges_expression[edge][0] and self.edges_expression[remain_edge][1] == self.edges_expression[edge][1]:
                        raise Exception(f"{self.graph_type} can not have multiple edges")
            if self.graph_type != "DIGRAPH":
                for remain_edge in range(edge + 1,len(self.edges_expression)):
                    if self.edges_expression[remain_edge][0] == self.edges_expression[edge][1] and self.edges_expression[remain_edge][1] == self.edges_expression[edge][0]:
                        raise Exception(f"{self.graph_type} can not have multiple edges")
            

        if id in symbol_table.symbols.keys(): #TODO: Create an object of type networkx
            symbol_table.update(Symbol(self.id,self.graph_type,[self.vertex, self.edges_expression])) 
        else:
            symbol_table.add(Symbol(self.id,self.graph_type,[self.vertex, self.edges_expression])) 

class If(Node) :
    def __init__(self,  logic_expression, node_list) :
        self.logic_expression = logic_expression
        self.node_list = node_list

    def evaluate(self, st): #TODO not implemented
        pass
