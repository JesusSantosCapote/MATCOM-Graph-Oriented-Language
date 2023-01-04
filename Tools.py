import networkx as nx
import matplotlib.pyplot as plt


def union_rara(graph1, graph2):
    graph1_node_number = len(graph1.nodes())
    graph2_node_number = len(graph2.nodes())
    graph1_node_attr = list(graph1._node.values())
    graph2_node_attr = list(graph2._node.values())

    union_vertex1 = [(i, graph1_node_attr[i]) for i in range(graph1_node_number)] 
    union_vertex2 = [(i + graph1_node_number, graph2_node_attr[i]) for i in range(graph2_node_number)]
    final_vertexs = union_vertex1 + union_vertex2

    union_edges1 = [(u, v, graph1.get_edge_data(u, v)) for u, v in graph1.edges()]
    union_edges2 = [(u + graph1_node_number, v + graph1_node_number, graph2.get_edge_data(u, v)) for u, v in graph2.edges()]
    final_edges = union_edges1 + union_edges2

    union_graph = nx.Graph()
    union_graph.add_nodes_from(final_vertexs)
    union_graph.add_edges_from(final_edges)

    return union_graph


def union(graph1, graph2):
    return nx.operators.compose(graph1, graph2)

#TODO: intersection needs to be fixed
def intersection(graph1, graph2):
    return nx.operators.intersection(graph1, graph2)


def difference(graph1, graph2):
    graph2_nodes = graph2.nodes
    graph1_nodes = graph1.nodes

    graph_diff = graph1.copy()
    
    nodes_to_delete = [node for node in graph2_nodes if node in graph1_nodes]

    graph_diff.remove_nodes_from(nodes_to_delete)

    return graph_diff


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

Graph_Operations={
    'union' : union,
    'intersection' : intersection,
    'difference' : difference
}


# a = nx.Graph([('pepe', 2), ('kuko', 'nosy')])
# # a.add_nodes_from([(0, {'color':'red'}), (1, {'color':'blue'}), (2, {'age': 60})])
# # a.add_edges_from([(0,1, {"weigth":5}), (0,2, {"code":5}), (0,0), (0,1)])

# b = nx.Graph([('pepe', 2), ('kuko', 'nosy'), ('nosy', 1)])
# # b.add_nodes_from([(0, {'color':'black'}), (1, {'audio':'stereo'}), (2, {'age': 50})])
# # b.add_edges_from([(0,1,{"weigth":5, "code":123}), (2, 3,{"weigth":5}), (0,1)])

# # c = union(a, b)

# d = nx.Graph([(5,0), (7,2), (2,0), (4, 5)])
# e = nx.Graph([(2,0), (7,2)])

# print(d.nodes)
# print(e.nodes)

# c = difference(d, e)

# print(c._node)
# print(c.edges)
