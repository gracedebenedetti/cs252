from structures.edge import Edge
from structures.graph import Graph
'''
christofides.py

Grace de Benedetti and John Witte implementation of Christofides' Algorithm for CS252: Algorithms

June 7th, 2021
'''
def read_data_to_graph(paths):
    '''
    Reads paths into a Graph component

    -> RETURNS Graph
    '''
    # Initialize empty edge and vertices sets
    edges = []
    vertices = []

    # Iterate through each path
    for path in paths:
        edge = path.split(',')

        # Add to vertices
        if edge[0] not in vertices:
            vertices.append(edge[0])
        if edge[1] not in vertices:
            vertices.append(edge[1])

        # Add an edge
        edge = Edge(edge[0], edge[1], int(edge[2]))
        edges.append(edge)

    return Graph(edges, vertices)

def find_mst(graph, origin):
    '''
    Finds a minimum spanning tree of a graph using a variation of Prim's algorithm

    -> RETURNS Graph
    '''
    # Initialize a new Graph as our MST representation
    mst = Graph([],[origin])
    graph_vertices = graph.get_vertices()

    while len(mst.get_vertices()) < len(graph_vertices):

        # Find the cheapest edge between the MST subset and the rest of the graph
        cheapest_edge = find_cheapest_edge(mst.get_vertices(), graph)
        mst.add_edge(cheapest_edge)

    return mst

def find_cheapest_edge(subset_vertices, graph):
    '''
    Given a subset of vertices from a graph, finds the cheapest edge connecting
    that subset to the rest of the graph

    -> RETURNS Edge
    '''
    edges = graph.get_edges_by_vertices(subset_vertices)
    for edge in edges:
        if edge.get_location_one() in subset_vertices and edge.get_location_two() not in subset_vertices:
            return edge
        if edge.get_location_two() in subset_vertices and edge.get_location_one() not in subset_vertices:
            return edge


def get_odd_degree_vertices(graph):
    '''
    Finds all the vertices in a graph with an odd degree

    -> RETURNS [string]
    '''
    vertices = graph.get_vertices()
    adjacency = graph.get_adjacency()
    odd_degree_vertices = []
    for vertex in vertices:
        if len(adjacency[vertex]) % 2 != 0:
            odd_degree_vertices.append(vertex)
    return odd_degree_vertices


def minimum_weight_matching(odd_degree_vertices, graph):
    '''
    Given a graph and a set of vertices, finds a subgraph with only the vertices
    and edges in question and finds a minimum cost perfect matching

    -> RETURNS [Edge]
    '''
    # Create a subgraph
    all_edges = graph.get_edges()
    sub_graph = Graph([],[])
    for edge in all_edges:
        if edge.get_location_one() in odd_degree_vertices and edge.get_location_two() in odd_degree_vertices:
            sub_graph.add_edge(edge)

    # Find the cheapest cost matching
    least_cost = 0
    edges = []

    # Iterate through all possible combinations of edges
    for pairs in all_vertex_pairs(odd_degree_vertices):
        cost = 0
        potential_edges = []

        # Iterate through the different edges of the current combination
        for pair in pairs:
            loc_one = pair[0]
            loc_two = pair[1]
            edge = sub_graph.get_edge(loc_one, loc_two)
            cost += edge.get_weight()
            potential_edges.append(edge)

        # If we have found a cheaper path, set it as such
        if cost < least_cost or least_cost == 0:
            least_cost = cost
            edges = potential_edges

    return edges


def all_vertex_pairs(vertices):
    '''
    Recursive function to generate all possible combinations of pairs

    -> RETURNS [[(string, string)]]
    '''
    # Help with approaches to this section from stack overflow
    if len(vertices) < 2:
        yield []
        return
    curr_vertex = vertices[0]
    for i in range(1, len(vertices)):
        pair = [curr_vertex, vertices[i]]
        for other_pairs in all_vertex_pairs(vertices[1: i] + vertices[i + 1:]):
            return [pair] + other_pairs


def fleurys(graph):
    '''
    Runs fleury's algorithm to find a Eulerian Tour of a graph

    -> RETURNS [Edge]
    '''
    curr_vertex = graph.get_vertices()[0]
    euler_path = []
    while len(graph.get_edges()) != 0:
        possible_edges = graph.get_edges_by_vertices([curr_vertex])

        # Loop through potential next stops
        for edge in possible_edges:
            destination = edge.get_location_one() if edge.get_location_one() != curr_vertex else edge.get_location_two()
            adjacency = graph.get_adjacency()

            # Find an edge that is not a bridge
            if len(adjacency[curr_vertex]) == 1 or len(adjacency[destination]) > 1:
                # If we find an edge, add it to our path and remove it from
                # our multigraph
                curr_vertex = destination
                euler_path.append(edge)
                graph.remove_edge(edge)
                break

    return euler_path

def hamiltonian(edges, origin):
    '''
    Finds a hamiltonian circuit from a Eulerian Path and prints the route
    '''
    visited = {}
    order = []
    count = 1

    # Look at each edge
    for edge in edges:

        # Only print if we haven't been there
        if edge.get_location_one() not in visited:
            print('%s. ' % count + edge.get_location_one())
            count += 1
            visited[edge.get_location_one()] = True

        # Only print if we haven't been there
        if edge.get_location_two() not in visited:
            print('%s. ' % count + edge.get_location_two())
            count += 1
            visited[edge.get_location_two()] = True

    # Print the origin
    print('%s. ' % count + origin)


if __name__ == '__main__':
    # Split data and read into initial structures
    paths = [line.strip() for line in open('paths.txt')]
    origin = paths[0].split(':')[1]
    paths = paths[1:]
    graph = read_data_to_graph(paths)

    # Find an MST
    mst = find_mst(graph, origin)

    # Get odd degree vertices
    odd_degree_vertices = get_odd_degree_vertices(mst)

    # Find edges with minimum cost and add to the MST to create a multigraph
    minimum_matching_edges = minimum_weight_matching(odd_degree_vertices, graph)
    mst.add_edges(minimum_matching_edges)

    # Find a eulerian tour of our multigraph
    eulerian_tour = fleurys(mst)

    # Find a hamiltonian circuit of our eulerian tour and print the path
    hamiltonian(eulerian_tour, origin)
