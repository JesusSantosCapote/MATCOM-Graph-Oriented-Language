import networkx as nx
from Tools import *

dic1 = {'Luka' : 'perro', 'Chuchi' : 'humano'}
dic2 = dic1.copy()
print(dic1)
print(dic2)
dic2['Chuchi'] = 'singado'
print(dic1)
print(dic2)

a = nx.Graph([('pepe', 2), ('kuko', 'nosy')])
a.add_nodes_from([(0, {'color':'red'}), (1, {'color':'blue'}), (2, {'age': 60})])
a.add_edges_from([(0,1, {"weigth":5}), (0,2, {"code":5}), (0,0), (0,1)])

print(a._node)
print(a.edges)

b = nx.Graph([('pepe', 2), ('kuko', 'nosy'), ('nosy', 1)])
b.add_nodes_from([(0, {'color':'black'}), (1, {'audio':'stereo'}), (2, {'age': 50})])
b.add_edges_from([(0,1,{"weigth":5, "code":123}), (2, 3,{"weigth":5}), (0,1)])

print(b._node)
print(b.edges)

c = intersection(a, b)

d = nx.Graph([(5,0), (7,2), (2,0), (4, 5)])
e = nx.Graph([(2,0), (7,2)])

print(d.nodes)
print(e.nodes)

c = difference(d, e)

print(c._node)
print(b.edges)