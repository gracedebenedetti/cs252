'''
Simple data class to store information about an edge of a graph
'''
class Edge:
    def __init__(self, location_one, location_two, weight):
        self.location_one = location_one
        self.location_two = location_two
        self.weight = weight

    def get_location_one(self):
        return self.location_one

    def get_location_two(self):
        return self.location_two

    def get_weight(self):
        return self.weight
