'''
Simple data class to store information about a graph
'''
class Graph:
    def __init__(self, edges, vertices):
        self.edges = edges

        # Create adjacency dictionary upon creation
        self.adjacent_vertices = {}
        for edge in edges:
            self.add_adjacency(edge.get_location_one(), edge.get_location_two())
        self.vertices = vertices

    '''
    Get method for vertices

    -> RETURNS [string]
    '''
    def get_vertices(self):
        return self.vertices

    '''
    Get method for edges

    -> RETURNS [Edge]
    '''
    def get_edges(self):
        return self.edges

    '''
    Get method for adjacency dictionary

    -> RETURNS {string: [string]}
    '''
    def get_adjacency(self):
        return self.adjacent_vertices

    '''
    Gets all edges for a list of vertices

    -> RETURNS [Edge]
    '''
    def get_edges_by_vertices(self, vertices):
        edges = self.edges
        edges = list(filter(lambda e:
            e.get_location_one() in vertices or
            e.get_location_two() in vertices, edges))
        edges.sort(key=lambda e: e.get_weight())
        return edges

    '''
    Adds an edge to the graph
    '''
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
        self.edges = edges

    '''
    Adds a list of edges to the graph
    '''
    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge)

    '''
    Removes an edge from the graph
    '''
    def remove_edge(self, edge):
        edges = self.edges
        edges.remove(edge)
        self.edges = edges
        adjacency = self.adjacent_vertices
        adjacency[edge.get_location_one()].remove(edge.get_location_two())
        adjacency[edge.get_location_two()].remove(edge.get_location_one())
        self.adjacent_vertices = adjacency

    '''
    Adds a vertex to the graph
    '''
    def add_vertex(self, vertex):
        vertices = self.get_vertices()
        vertices.append(vertex)
        self.vertices = vertices

    '''
    Adds to the adjacency dictionary for two vertices
    '''
    def add_adjacency(self, vertex_one, vertex_two):
        if vertex_one not in self.adjacent_vertices:
            self.adjacent_vertices[vertex_one] = []
        if vertex_two not in self.adjacent_vertices:
            self.adjacent_vertices[vertex_two] = []
        if vertex_two not in self.adjacent_vertices[vertex_one]:
            self.adjacent_vertices[vertex_one].append(vertex_two)
        if vertex_one not in self.adjacent_vertices[vertex_two]:
            self.adjacent_vertices[vertex_two].append(vertex_one)

    '''
    Gets the edge between two vertices
    '''
    def get_edge(self, location_one, location_two):
        edges = list(filter(lambda e:
            e.get_location_one() in [location_one, location_two] and
            e.get_location_two() in [location_one, location_two], self.edges))
        return edges[0]
