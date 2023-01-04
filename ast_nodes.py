from abc import ABC, abstractmethod
import networkx as nx
from symbol_table import DataType
from exceptions import SemanticException
from symbol_table import *
import matplotlib.pyplot as plt

class Node(ABC):
    @abstractmethod
    def evaluate(self, st):
        pass       

#TODO que todos reciban una linea la crearse

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
        symbol = symbol_table.symbols[self.graph_id]
        if symbol.data_type not in ["digraph", "multigraph", "pseudograph", "graph"]:
            raise SemanticException(self.line, 'plot error : plot argument must be a type of graph')

        nx.draw(symbol.value, with_labels=True, font_weight='bold')
        plt.show()


class Assign(Node) :

    def __init__(self, id, graph_type, vertex, edges_expression) :
        self.id = id
        self.graph_type = graph_type
        self.vertex = vertex
        self.edges_expression = edges_expression

    
    def build_graph(self):
        graph = None
        if self.graph_type == "multigraph":
            graph = nx.MultiGraph()
        elif self.graph_type == "digraph":
            graph = nx.DiGraph()
        else:
            graph = nx.Graph()
        
        graph.add_nodes_from(range(self.vertex))

        for edge in self.edges_expression:
            graph.add_edge(edge[0], edge[1])
            graph[edge[0]][edge[1]]['weight'] = edge[2]

        return graph

#TODO Hasta ahora solo podemos crear grafos normales
    def evaluate(self, symbol_table : SymbolTable):
        
        for edge in range (len(self.edges_expression)):
            if self.edges_expression[edge][0] >= self.vertex or self.edges_expression[edge][0] < 0 or self.edges_expression[edge][1] >= self.vertex or self.edges_expression[edge][1] < 0:
                raise Exception("Edge non-existent")
            if self.graph_type != "pseudograph":
                if self.edges_expression[edge][0] == self.edges_expression[edge][1]:
                    raise Exception(f"{self.graph_type} can not have loop edges")
            if self.graph_type != "multigraph":
                for remain_edge in range(edge + 1, len(self.edges_expression)):
                    if self.edges_expression[remain_edge][0] == self.edges_expression[edge][0] and self.edges_expression[remain_edge][1] == self.edges_expression[edge][1]:
                        raise Exception(f"{self.graph_type} can not have multiple edges")
            if self.graph_type != "digraph":
                for remain_edge in range(edge + 1,len(self.edges_expression)):
                    if self.edges_expression[remain_edge][0] == self.edges_expression[edge][1] and self.edges_expression[remain_edge][1] == self.edges_expression[edge][0]:
                        raise Exception(f"{self.graph_type} can not have multiple edges")
            
        graph = self.build_graph()

        if id in symbol_table.symbols.keys():
            symbol_table.update(Symbol(self.id, self.graph_type, graph)) 
        else:
            symbol_table.add(Symbol(self.id, self.graph_type, graph)) 


class If(Node) :
    def __init__(self,  logic_expression, instructions) :
        self.logic_expression = logic_expression
        self.instructions = instructions

    def evaluate(self, st): #TODO Implement local symbol_table for if instruction
        if self.logic_expression:
            for instruction in self.instructions.node_list:
                instruction.evaluate(st)


class GraphOperAssign(Node):
    def __init__(self, operation, id1, id2, store_id, line) -> None:
        self.id1 = id1
        self.id2 = id2
        self.operation = operation
        self.line = line
        self.store_id = store_id


    def evaluate(self, st):
        symbol1 = st.symbols[self.id1]
        if symbol1.data_type not in ["digraph", "multigraph", "pseudograph", "graph"]:
            raise TypeError(f"{self.operation} error at line {self.line}: variable {self.id1} must hava a type of graph")

        symbol2 = st.symbols[self.id2]
        if symbol2.data_type not in ["digraph", "multigraph", "pseudograph", "graph"]:
            raise TypeError(f"{self.operation} error at line {self.line}: variable {self.id2} must hava a type of graph")

        if symbol1.data_type != symbol2.data_type:
            raise TypeError(f"{self.operation} error at line {self.line}: {self.id1} and {self.id2} they are not the same type of graph")

        


