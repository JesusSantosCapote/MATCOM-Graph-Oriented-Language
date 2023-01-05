import networkx as nx
from Tools import *

a = nx.Graph()
a.add_nodes_from([(0, {'color': 'red'}), ((1, {'age':2})), 2])
a.add_edges_from([(0,1, {'weight':5}), (0,2, {'weight':4, 'code': 42}), (1,2, {'weight':40})])

b = nx.traversal.bfs_tree(a, 2)

for node,d in a.nodes(data=True):
    b.add_nodes_from([(node, d)])

for u,v in b.edges():
    attr = a.get_edge_data(u, v)
    for key, value in attr.items():
        b[u][v][key] = value

print(b.nodes(data=True))
print(b.edges(data=True))
print()
print(a.nodes(data=True))
print(a.edges(data=True))
