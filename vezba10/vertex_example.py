from enum import Enum	

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, name, c = None, p = None, d1 = None, d2 = None, d = None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.c = c
        self.name = name
        self.p = p
        self.d1 = d1
        self.d2 = d2
        self.d = d

    def __str__(self):
        string = "Vertex " + self.name + ":\n"
        string+="Connected with: "
        for i in range (len(self.d1)):
            string+=self.d1[i].name + " (" + self.d2[i] + ")"
        string+="\n\n"
        return string
        

class Edge:

    def __init__(self, src = None, dst = None, wt = None):
        self.src = src
        self.dst = dst
        self.wt = wt
	
class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255		
		
u = Vertex(c=VertexColor.WHITE, d1=1, d2=22)
v = Vertex(c=VertexColor.GRAY, p=u, d1=33, d2=4)



def initializeSingleSource(G, s):
    for i in G:
        i.d = math.inf
        i.p = None
    s.d = 0

def relax(u, v, w):
    for i in range(len(w)):
        if(w[i].src == u & w[i].dst == v):
            wt = w[i].wt
            break

    if(v.d > u.d + wt):
        v.d = u.d + wt
        v.p = u

def dijkstra(G, w, s):
    initializeSingleSource(G, s)
    s = []
    Q = G
    while(len(Q) > 0):
        u = extractMin(Q)
        s.append(u)
        for i in u.d1:
            relax(u, i, w)

def extractMin(ls):
    min = math.inf
    for i in ls:
        if(ls.d < min):
            min = ls.d
    return min

s = Vertex('s')
t = Vertex('t')
x = Vertex('x')
y = Vertex('y')
z = Vertex('z')

s.d1 = [t, y]
s.d2 = [10, 5]

t.d1 = [x, y]
t.d2 = [1, 2]

x.d1 = [z]
x.d2 = [4]

y.d1 = [t, x, z]
y.d2 = [3, 9, 2]

z.d1 = [s, x]
z.d2 = [7, 6]


edges = []

edges.append(Edge(s, t, 10))
edges.append(Edge(s, y, 5))
edges.append(Edge(t, x, 1))
edges.append(Edge(t, y, 2))
edges.append(Edge(x, z, 4))
edges.append(Edge(y, t, 3))
edges.append(Edge(y, x, 9))
edges.append(Edge(y, z, 2))
edges.append(Edge(z, s, 7))
edges.append(Edge(z, x, 6))


print(t)