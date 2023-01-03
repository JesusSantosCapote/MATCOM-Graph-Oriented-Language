from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def evaluate(self):
        pass       


class Instructions(Node):
    def __init__(self, node_list) -> None:
        self.node_list = node_list

    def evaluate(self):
        for instruction in self.node_list:
            instruction.evaluate


class Plot(Node) :

    def __init__(self,  graph) :
        self.graph = graph

    def evaluate(self): #TODO not implemented
        pass


class Assign(Node) :
    '''
        Esta clase representa la instrucción de asignación de variables
        Recibe como parámetro el identificador a asignar y el valor que será asignado.
    '''

    def __init__(self, id, graph_type, vertex, edges_expression) :
        self.id = id
        self.graph_type = graph_type
        self.vertex = vertex
        self.edges_expression = edges_expression