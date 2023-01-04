import networkx as nx
import matplotlib.pyplot as plt

Bool_Operations={
    '==' : lambda x,y : x==y,
    '>' : lambda x,y : x>y,
    '<' : lambda x,y : x<y,
    '>=' : lambda x,y : x>=y,
    '<=' : lambda x,y : x<=y,
    '!=' : lambda x,y : x!=y,
}

Arithmetic_Operations={
    '+' : lambda x,y : x+y,
    '-' : lambda x,y : x-y,
    '*' : lambda x,y : x*y,
    '/' : lambda x,y : x/y,
}

def union(graph1, graph2):
    graph1_node_number = len(graph1.nodes())
    graph2_node_number = len(graph2.nodes())
    new_vertex = [i for i in range(graph1_node_number + graph2_node_number)]


a = nx.Graph()
#a.add_nodes_from([(0, {'color':'red'}), (1, {'color':'blue'}), (2, {'age': 60})])
a.add_nodes_from([0, 1, 2])
a.add_edges_from([(0,1), (0,2), (0,0), (0,1)])

a[0][1]['w'] = 0
a[0][2]['w'] = 0

print(a._node)
print(a.edges())

b = nx.Graph([(0,1), (2, 3), (0,1)])
print(b.edges())


c = nx.union(a, b, rename=("a-", "b-"))

print(c.edges())
