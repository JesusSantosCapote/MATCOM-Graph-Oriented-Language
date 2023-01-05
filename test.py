import networkx as nx
from Tools import *

a = nx.Graph()
a.add_nodes_from([(0, {'color': 'red'}), ((1, {'age':2})), 2])
a.add_edges_from([(0,1, {'weight':5}), (0,2, {'weight':4, 'code': 42}), (1,2, {'weight':40})])

b = nx.tree.minimum_spanning_tree(a)
print(nx.dijkstra_path(a,1,2,"weight"))
# print(b.nodes(data=True))
# print(b.edges(data=True))

# print(a.nodes(data=True))
# print(a.edges(data=True))
