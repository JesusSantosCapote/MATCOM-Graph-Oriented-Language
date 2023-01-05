from abc import ABC, abstractmethod
import networkx as nx
from symbol_table import DataType
from exceptions import SemanticException
from symbol_table import *
import matplotlib.pyplot as plt
import pylab
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

    def __init__(self, graph_expression_object, line) :
        self.graph_expression_object = graph_expression_object
        self.line = line

    def evaluate(self, st):
        graph = self.graph_expression_object.evaluate(st)
        nx.draw(graph, with_labels=True, font_weight='bold')
        plt.show()


class K_color_plot (Node) :

    def __init__(self, graph_expression_object, line) :
        self.graph_expression_object = graph_expression_object
        self.line = line
    
    def evaluate(self, st):
        graph = self.graph_expression_object.evaluate(st)
        colors = k_color(graph)

        nx.draw_networkx(graph, labels=colors)
        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()


class Weighted_plot (Node) :

    def __init__(self, graph_expression_object, line) :
        self.graph_expression_object = graph_expression_object
        self.line = line
    
    def evaluate(self, st):
        graph = self.graph_expression_object.evaluate(st)
        
        pos = nx.layout.circular_layout(graph)
        pylab.figure(2)
        nx.draw(graph,pos)
        nx.draw_networkx_labels(graph, pos)
        # specifiy edge labels explicitly
        edge_labels=dict([((u,v,),d['weight']) for u,v,d in graph.edges(data=True)])
        nx.draw_networkx_edge_labels(graph,pos,edge_labels=edge_labels)

        # show graphs
        pylab.show()

    
class Unary_graph_operation(Node):


    def __init__(self, graph_expression_object, operation):
        self.graph_expression_object = graph_expression_object
        self.operation = operation

    def evaluate(self, st):
        graph = self.graph_expression_object.evaluate(st)
        return Graph_Operations[self.operation](graph)

#TODO: Finish MST.evaluate() implementation
class MST(Node):
    
    def __init__(self, graph_expression_object, operation, line) :
        self.graph_expression_object = graph_expression_object
        self.operation = operation
        self.line = line
        
    def evaluate(self, st):
        graph = self.graph_expression_object.evaluate(st)
        if graph.is_directed():
            raise TypeError(f"At line {self.line}. Kruskal can't recive digraph object.")


class Binary_graph_operation(Node):
    
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


class Contain_vertex(Node):

    def __init__(self, graph_expression_object, value_expression_object):
        self.graph_expression_object = graph_expression_object
        self.value_expression_object = value_expression_object

    def evaluate(self, st):
        graph = self.graph_expression_object.evaluate(st)
        vertex = self.value_expression_object.evaluate(st)
        return contain_vertex(graph, vertex)


class Contain_edges(Node):

    def __init__(self, graph_expression_object, edge_expression) :
        self.graph_expression_object = graph_expression_object
        self.edge_expression = edge_expression

    def evaluate(self, st):
        graph = self.graph_expression_object.evaluate(st)
        return contain_edges(graph, self.edge_expression)

class Unary_function(Node):


    def __init__(self, graph_expression_object, function, line) :
        self.graph_expression_object = graph_expression_object
        self.function = function
        self.line = line


    def evaluate(self, st : SymbolTable):
        graph = self.graph_expression_object.evaluate(st)
        return Graph_Unary_Functions[self.function](graph)

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

        for vertex in list(graph.nodes):
            graph.nodes[vertex]['color'] = 1

        for edge in self.edges_expression:
            graph.add_edge(edge[0], edge[1])
            graph[edge[0]][edge[1]]['weight'] = edge[2]

        return graph

    def evaluate(self, st):
        self.vertex = self.vertex.evaluate(st)
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

        for vertex in graph.nodes:
            graph.nodes[vertex]['color'] = 1
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


class Create_Graph_With_Variable(Node):
    def __init__(self, variable_id, line) :
        self.variable_id = variable_id
        self.line = line
    

    def evaluate(self, st):
        recover_object = st.get(self.variable_id, self.line)
        if recover_object.data_type != 'graph' and recover_object.data_type != 'digraph':
            raise TypeError(f"At line {self.line}. {self.id} was not a graph type object.")
        graph = recover_object.value
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


class Add_vertex(Node) :

    def __init__(self, id, vertexs_expression, line) :
        self.id = id
        self.vertexs_expression = vertexs_expression
        self.line = line

    def evaluate(self, st : SymbolTable):
        recover_object = st.get(self.id, self.line)
        if recover_object.data_type != 'graph' and recover_object.data_type != 'digraph':
            raise TypeError(f"At line {self.line}. {self.id} was not a graph type object.")
        graph = recover_object.value
        graph.add_nodes_from(self.vertexs_expression)

class Add_edge(Node) :

    def __init__(self, id, edges_expression, line) :
        self.id = id
        self.edges_expression = edges_expression
        self.line = line

    def evaluate(self, st : SymbolTable):
        recover_object = st.get(self.id, self.line)
        if recover_object.data_type != 'graph' and recover_object.data_type != 'digraph':
            raise TypeError(f"At line {self.line}. {self.id} was not a graph type object.")
        graph = recover_object.value
        for edge in self.edges_expression:
            graph.add_edge(edge[0], edge[1])
            graph[edge[0]][edge[1]]['weight'] = edge[2]


class Add_vertex_and_edge(Node) :

    def __init__(self, id, vertexs_expression, edges_expression, line):
        self.vertex_add = Add_vertex(id, vertexs_expression, line)
        self.edge_add = Add_edge(id, edges_expression, line)

    def evaluate(self, st):
        self.vertex_add.evaluate(st)
        self.edge_add.evaluate(st)


class If(Node) :
    def __init__(self,  logic_expression, instructions) :
        self.logic_expression = logic_expression
        self.instructions = instructions

    def evaluate(self, st):
        solved_logic_expression = self.logic_expression.evaluate(st)
        if solved_logic_expression:
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
        solved_logic_expression = self.logic_expression.evaluate(st)
        if solved_logic_expression:
            instructions = self.instructions_if_true
        else:
            instructions = self.instructions_if_false
        new_st = st.Clone()
        for instruction in instructions.node_list:
            instruction.evaluate(new_st)
        for key in st.symbols.keys():
            st.update(new_st.symbols[key])

#TODO: Use of iterable object in forvertex and foredge
class For_vertex(Node) :
    def __init__(self, iterator, graph, instructions, line) :
        self.iterator = iterator
        self.graph = graph
        self.instructions = instructions
        self.line = line
    
    def evaluate(self, st):
        new_st = st.Clone()
        graph_data = st.get(self.graph, self.line)
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


class Numerical_value(Node):

    def __init__(self, value) :
        self.value = value

    def evaluate(self, st):
        return self.value

class Algebraic_expression(Node):

    def __init__(self, exp1, exp2, operation) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operation = operation

    def evaluate(self, st):
        solved_exp1 = self.exp1.evaluate(st)
        solved_exp2 = self.exp2.evaluate(st)
        return Arithmetic_Operations[self.operation](solved_exp1,solved_exp2)

class Minus_operation(Node):

    def __init__(self, exp) :
        self.exp = exp

    def evaluate(self, st):
        value = self.exp.evaluate(st)
        return -value

class Bool_Operation(Node):

    def __init__(self, exp1, exp2, operator) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operator = operator

    def evaluate(self, st):
        solved_exp1 = self.exp1.evaluate(st)
        solved_exp2 = self.exp2.evaluate(st)
        return Bool_Operations[self.operator](solved_exp1,solved_exp2)

class Solve(Node):
    def __init__(self, item) :
        self.item = item
    def evaluate(self, st):
        return self.item.evaluate(st)