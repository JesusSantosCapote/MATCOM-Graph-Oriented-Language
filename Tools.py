import networkx as nx
import matplotlib.pyplot as plt

#TODO: union_rara needs to be fixed
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


def intersection(graph1, graph2):
    graph1_copy = graph1.copy()
    graph2_copy = graph2.copy()

    common_nodes = [node for node in graph1_copy.nodes if node in graph2_copy.nodes]
    common_edges = [(u, v) for u, v in graph1_copy.edges if graph2_copy.has_edge(u, v)]
    intersec_nodes = []
    intersec_edges = []
    
    for node in common_nodes:
        attr2 = graph2_copy._node[node]
        attr1 = graph1_copy._node[node]

        for key, value in attr1.items():
            attr2[key] = value

        intersec_nodes.append((node, attr2))

    for u, v in common_edges:
        edge_attr2 = graph2_copy.get_edge_data(u, v)
        edge_attr1 = graph1_copy.get_edge_data(u, v)

        for key, value in edge_attr1.items():
            edge_attr2[key] = value

        intersec_edges.append((u, v, edge_attr2))

    graph1_copy.clear()

    graph1_copy.add_nodes_from(intersec_nodes)
    graph1_copy.add_edges_from(intersec_edges)

    return graph1_copy


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
