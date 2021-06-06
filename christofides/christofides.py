from structures.edge import Edge
from structures.graph import Graph
'''
christofides.py

Grace de Benedetti and John Witte implementation of Christofides' Algorithm for CS252: Algorithms

June 7th, 2021
'''

def read_data_to_graph():
    "reads paths and weights from data file into dictionary"
    paths = [line.strip().lower() for line in open('paths.txt')]
    edges = []
    vertices = []

    for path in paths:
        edge = path.split(',')

        if edge[0] not in vertices:
            vertices.append(edge[0])
        if edge[1] not in vertices:
            vertices.append(edge[1])

        edge = Edge(edge[0], edge[1], int(edge[2]))
        edges.append(edge)

    return Graph(edges, vertices)

def find_mst(graph):
    graph_vertices = graph.get_vertices()
    mst_vertices = []

    vertex = 'e'
    mst = Graph([],[vertex])
    while len(mst.get_vertices()) < len(graph_vertices):
        cheapest_edge = find_cheapest_edge(mst.get_vertices(), graph_vertices, graph)
        mst.add_edge(cheapest_edge)
    return mst

def find_cheapest_edge(subset_vertices, set_vertices, graph):
    edges = graph.get_edges_by_vertices(subset_vertices)
    for edge in edges:
        if edge.get_location_one() in subset_vertices and edge.get_location_two() not in subset_vertices:
            return edge
        if edge.get_location_two() in subset_vertices and edge.get_location_one() not in subset_vertices:
            return edge


def get_odd_degree_vertices(graph):
    vertices = graph.get_vertices()
    adjacency = graph.get_adjacency()
    odd_degree_vertices = []
    for vertex in vertices:
        if len(adjacency[vertex]) % 2 != 0:
            odd_degree_vertices.append(vertex)
    return odd_degree_vertices


def minimum_weight_matching(odd_degree_vertices, graph):
    edges = graph.get_edges_by_vertices()


#Eulerian tour

#Hamiltonian circuit


if __name__ == '__main__':
    graph = read_data_to_graph()
    mst = find_mst(graph)
    odd_degree_vertices = get_odd_degree_vertices(mst)
    minimum_weight_matching(odd_degree_vertices, graph)


    #for edge in mst_edges:
        #print(edge.get_location_one() + ' ' + edge.get_location_two() + ' ' + str(edge.get_weight()))
