'''
Simple data class to store information about a graph
'''
class Graph:
    def __init__(self, edges, vertices):
        self.edges = edges

        self.adjacent_vertices = {}
        for edge in edges:
            self.add_adjacency(edge.get_location_one(), edge.get_location_two())

        self.vertices = vertices

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def get_adjacency(self):
        return self.adjacent_vertices

    def get_edges_by_vertices(self, vertices):
        edges = self.edges
        edges = list(filter(lambda e:
            e.get_location_one() in vertices or
            e.get_location_two() in vertices, edges))
        edges.sort(key=lambda e: e.get_weight())
        for edge in edges:
            print(edge.get_weight())
        print('')
        return edges

    def add_edge(self, edge):
        location_one = edge.get_location_one()
        location_two = edge.get_location_two()
        if location_one not in self.vertices:
            self.add_vertex(location_one)
        if location_two not in self.vertices:
            self.add_vertex(location_two)
        self.add_adjacency(location_one, location_two)
        edges = self.edges
        edges.append(edge)
        return edges

    def add_vertex(self, vertex):
        vertices = self.get_vertices()
        vertices.append(vertex)
        self.vertices = vertices

    def add_adjacency(self, vertex_one, vertex_two):
        if vertex_one not in self.adjacent_vertices:
            self.adjacent_vertices[vertex_one] = []
        if vertex_two not in self.adjacent_vertices:
            self.adjacent_vertices[vertex_two] = []
        if vertex_two not in self.adjacent_vertices[vertex_one]:
            self.adjacent_vertices[vertex_one].append(vertex_two)
        if vertex_one not in self.adjacent_vertices[vertex_two]:
            self.adjacent_vertices[vertex_two].append(vertex_one)
