'''
Simple data class to store information about an edge of a graph
'''
class Vertex:
    def __init__(self, label):
        self.label = label

    def get_label(self):
        return self.label
