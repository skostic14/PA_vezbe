class Vortex:
    def __init__(self, name = None, parent = None, color = None, dist = None):
        self.name = name
        self.parent = parent
        self.color = color
        self.dist = dist

    def __str__(self):
        return self.name

class Edge:
    def __init__(self, src = None, dst = None, weight = None):
        self.src = src
        self.dst = dst
        self.weight = weight

class Graph:
    def __init__(self, edges = None, vortices = None):
        self.edges = edges
        self.vortices = vortices
   
    def __str__(self):
        string = ""
        for i in self.vortices:
            string+=i
        return string