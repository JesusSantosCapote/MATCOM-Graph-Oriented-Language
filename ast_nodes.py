from abc import ABC, abstractmethod
import networkx as nx
from symbol_table import DataType
from exceptions import SemanticException
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

    def __init__(self, graph_id, line) :
        self.graph_id = graph_id
        self.line = line

    def evaluate(self, symbol_table): #TODO not implemented
        symbol = symbol_table[self.graph_id]
        if symbol.data_type not in [DataType.DIGRAPH, DataType.GRAPH, DataType.PSEUDOGRAPH]:
            raise SemanticException(self.line, 'plot error : plot argument must be a type of graph')

        nx.draw(symbol.value, with_labels=True, font_weight='bold')


class Assign(Node) :

    def __init__(self, id, graph_type, vertex, edges_expression) :
        self.id = id
        self.graph_type = graph_type
        self.vertex = vertex
        self.edges_expression = edges_expression

    def evaluate(self, symbol_table : SymbolTable):
        
        for edge in self.edges_expression: #TODO:This need to be fixed. For the iterations checking multiple-edges
            if edge[0] >= self.vertex or edge[0] < 0 or edge[1] >= self.vertex or edge[1] < 0:
                raise Exception("Edge non-existent")
            if self.graph_type != "PSEUDOGRAPH":
                if edge[0] == edge[1]:
                    raise Exception(f"{self.graph_type} can not have loop edges")
            if self.graph_type != "MULTIGRAPH":
                for remain_edge in range(edge,len(self.edges_expression)):
                    if remain_edge[0] == edge[0] and remain_edge[1] == edge[1]:
                        raise Exception(f"{self.graph_type} can not have multiple edges")
            if self.graph_type != "DIGRAPH":
                for remain_edge in range(edge,len(self.edges_expression)):
                    if remain_edge[0] == edge[1] and remain_edge[1] == edge[0]:
                        raise Exception(f"{self.graph_type} can not have multiple edges")
            

        if id in symbol_table.symbols.keys():
            symbol_table.update(Symbol(self.id,self.graph_type,[self.vertex, self.edges_expression])) 
        else:
            symbol_table.add(Symbol(self.id,self.graph_type,[self.vertex, self.edges_expression])) 


