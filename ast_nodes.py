from abc import ABC, abstractmethod
import networkx as nx
from symbol_table import DataType
from exceptions import SemanticException
from symbol_table import *
import matplotlib.pyplot as plt
from Tools import *

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

    def evaluate(self, symbol_table):
        symbol = symbol_table.symbols[self.graph_id]
        if symbol.data_type not in ["digraph", "multigraph", "pseudograph", "graph"]:
            raise SemanticException(self.line, 'plot error : plot argument must be a type of graph')

        nx.draw(symbol.value, with_labels=True, font_weight='bold')
        plt.show()


class Graph_operation(Node):
    
    def __init__(self, graph_expression_object1, graph_expression_object2, operation, line):
        self.graph_expression_object1 = graph_expression_object1
        self.graph_expression_object2 = graph_expression_object2
        self.operation = operation
        self.line = line
    
    def evaluate(self, st):
        graph1 = self.graph_expression_object1.evaluate(st)
        graph2 = self.graph_expression_object2.evaluate(st)
        if graph1.is_directed() == graph2.is_directed():
            return Graph_Operations[self.operation](graph1, graph2)
        else:
            raise TypeError(f"At line: {self.line}. The graph variables has different types")


class Create_graph(Node) :

    def __init__(self, graph_type, vertex, edges_expression, line) :
        self.graph_type = graph_type
        self.vertex = vertex
        self.edges_expression = edges_expression
        self.line = line

    def build_graph(self):
        graph = None
        if self.graph_type == "digraph":
            graph = nx.DiGraph()
        else:
            graph = nx.Graph()
        
        graph.add_nodes_from(range(self.vertex))

        for edge in self.edges_expression:
            graph.add_edge(edge[0], edge[1])
            graph[edge[0]][edge[1]]['weight'] = edge[2]

        return graph

    def evaluate(self, st):
        for edge in range (len(self.edges_expression)):
            if self.edges_expression[edge][0] >= self.vertex or self.edges_expression[edge][0] < 0 or self.edges_expression[edge][1] >= self.vertex or self.edges_expression[edge][1] < 0:
                raise Exception(f"At line {self.line}. Edge non-existent")
            if self.edges_expression[edge][0] == self.edges_expression[edge][1]:
                raise Exception(f"At line {self.line}. {self.graph_type} can not have loop edges")
            for remain_edge in range(edge + 1, len(self.edges_expression)):
                if self.edges_expression[remain_edge][0] == self.edges_expression[edge][0] and self.edges_expression[remain_edge][1] == self.edges_expression[edge][1]:
                    raise Exception(f"At line {self.line}.{self.graph_type} can not have multiple edges")
            if self.graph_type != "digraph":
                for remain_edge in range(edge + 1,len(self.edges_expression)):
                    if self.edges_expression[remain_edge][0] == self.edges_expression[edge][1] and self.edges_expression[remain_edge][1] == self.edges_expression[edge][0]:
                        raise Exception(f"At line {self.line}. {self.graph_type} can not have multiple edges")
            
        graph = self.build_graph()  
        return graph


class Create_graph_with_vertex(Node):
    def __init__(self, graph_type, vertexs_expression, edges_expression, line ) :
        self.graph_type = graph_type
        self.vertexs_expression = vertexs_expression
        self.edges_expression = edges_expression
        self.line = line


    def build_graph(self):
        graph = None
        if self.graph_type == "digraph":
            graph = nx.DiGraph()
        else:
            graph = nx.Graph()
        
        graph.add_nodes_from(self.vertexs_expression)

        for edge in self.edges_expression:
            graph.add_edge(edge[0], edge[1])
            graph[edge[0]][edge[1]]['weight'] = edge[2]

        return graph


    def evaluate(self, st):
        for edge in range (len(self.edges_expression)):
            if not self.edges_expression[edge][0] in self.vertexs_expression or not self.edges_expression[edge][1] in self.vertexs_expression:
                raise Exception(f"At line {self.line}. Edge non-existent")
            if self.edges_expression[edge][0] == self.edges_expression[edge][1]:
                raise Exception(f"At line {self.line}. {self.graph_type} can not have loop edges")
            for remain_edge in range(edge + 1, len(self.edges_expression)):
                if self.edges_expression[remain_edge][0] == self.edges_expression[edge][0] and self.edges_expression[remain_edge][1] == self.edges_expression[edge][1]:
                    raise Exception(f"At line {self.line}.{self.graph_type} can not have multiple edges")
            if self.graph_type != "digraph":
                for remain_edge in range(edge + 1,len(self.edges_expression)):
                    if self.edges_expression[remain_edge][0] == self.edges_expression[edge][1] and self.edges_expression[remain_edge][1] == self.edges_expression[edge][0]:
                        raise Exception(f"At line {self.line}. {self.graph_type} can not have multiple edges")
            
        graph = self.build_graph()  
        return graph


class Assign(Node) :

    def __init__(self, id, graph_expression_object) :
        self.id = id
        self.graph_expression_object = graph_expression_object
    def evaluate(self, symbol_table : SymbolTable):
        graph = self.graph_expression_object.evaluate(symbol_table)
        if graph.is_directed():
            graph_type = "digraph"
        else:
            graph_type = "graph"
        if id in symbol_table.symbols.keys():
            symbol_table.update(Symbol(self.id, graph_type, graph)) 
        else:
            symbol_table.add(Symbol(self.id, graph_type, graph)) 


class If(Node) :
    def __init__(self,  logic_expression, instructions) :
        self.logic_expression = logic_expression
        self.instructions = instructions

    def evaluate(self, st):
        if self.logic_expression:
            new_st = st.Clone()
            for instruction in self.instructions.node_list:
                instruction.evaluate(new_st)
            for key in st.symbols.keys():
                st.update(new_st.symbols[key])


class If_else(Node) :
    def __init__(self,  logic_expression, instructions_if_true, instructions_if_false) :
        self.logic_expression = logic_expression
        self.instructions_if_true = instructions_if_true
        self.instructions_if_false = instructions_if_false

    def evaluate(self, st):
        if self.logic_expression:
            instructions = self.instructions_if_true
        else:
            instructions = self.instructions_if_false
        new_st = st.Clone()
        for instruction in instructions.node_list:
            instruction.evaluate(new_st)
        for key in st.symbols.keys():
            st.update(new_st.symbols[key])


class For_vertex(Node) :
    def __init__(self, iterator, graph, instructions, line) :
        self.iterator = iterator
        self.graph = graph
        self.instructions = instructions
        self.line = line
    
    def evaluate(self, st):
        new_st = st.Clone()
        graph_data = st.get(self.graph)
        if graph_data.data_type == "graph" or graph_data.data_type == "digraph":
            for vertex in list(st.symbols[self.graph].value.nodes):
                print(vertex)
                new_st.add(Symbol(self.iterator,"vertex",vertex))
                for instruction in self.instructions.node_list:
                    instruction.evaluate(new_st)
                for key in st.symbols.keys():
                    st.update(new_st.symbols[key])
                new_st = st.Clone()
        else:
            raise TypeError(f"At line: {self.line}. {self.graph} is a {graph_data.data_type} variable, a graph variable was expected")


class For_edge(Node) :
    def __init__(self, iterator, graph, instructions, line) :
        self.iterator = iterator
        self.graph = graph
        self.instructions = instructions
        self.line = line
    
    def evaluate(self, st):
        new_st = st.Clone()
        graph_data = st.get(self.graph)
        if graph_data.data_type == "graph" or graph_data.data_type == "digraph":
            for edge in list(st.symbols[self.graph].value.edges):
                print(edge)
                new_st.add(Symbol(self.iterator,"edge",edge))
                for instruction in self.instructions.node_list:
                    instruction.evaluate(new_st)
                for key in st.symbols.keys():
                    st.update(new_st.symbols[key])
                new_st = st.Clone()
        else:
            raise TypeError(f"At line: {self.line}. {self.graph} is a {graph_data.data_type} variable, a graph variable was expected")
