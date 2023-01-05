import networkx as nx
from Tools import *

a = nx.Graph()

a.add_nodes_from([1,7,4])

a.is_directed()

for vertex in a.nodes:
    a.nodes[vertex]['color'] = 1

print(a._node)

        # for edge in self.edges_expression:
        #     graph.add_edge(edge[0], edge[1])
        #     graph[edge[0]][edge[1]]['weight'] = edge[2]
