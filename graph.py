import networkx as nx
import matplotlib.pyplot as plt

def show_graph(graph):
    edge_labels = {(u, v): d['weight'] for u, v, d in graph.edges(data=True)}
    pos = nx.spring_layout(graph)

    plt.figure(1)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red')
    plt.show()

GRAPH = nx.Graph()
GRAPH.add_nodes_from(range(1, 21))

edge_list = [
    (1, 2, {'weight': 5}),
    (2, 3, {'weight': 7}),
    (2, 6, {'weight': 2}),
    (3, 12, {'weight': 8}),
    (4, 5, {'weight': 3}),
    (5, 9, {'weight': 6}),
    (6, 7, {'weight': 5}),
    (6, 10, {'weight': 6}),
    (7, 11, {'weight': 6}),
    (8, 9, {'weight': 3}),
    (9, 10, {'weight': 2}),
    (10, 11, {'weight': 5}),
    (10, 15, {'weight': 2}),
    (11, 12, {'weight': 2}),
    (11, 20, {'weight': 9}),
    (12, 21, {'weight': 9}),
    (13, 14, {'weight': 3}),
    (14, 15, {'weight': 2}),
    (14, 18, {'weight': 7}),
    (15, 16, {'weight': 3}),
    (16, 19, {'weight': 7}),
    (17, 18, {'weight': 3}),
    (18, 19, {'weight': 5}),
    (19, 20, {'weight': 2}),
    (20, 21, {'weight': 2})
]
GRAPH.add_edges_from(edge_list)

print("The dijkstra algorithm will appear after you close the window")
print("If some message appear down bellow, it is just a warining. Take it easy")

show_graph(GRAPH)