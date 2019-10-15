from enum import Enum
import math
import random
import string

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
            string+=self.d1[i].name + "(" + str(self.d2[i]) + ") "
        string+="\n\n"
        return string
        

class Edge:

    def __init__(self, src = None, dst = None, wt = None):
        self.src = src
        self.dst = dst
        self.wt = wt

    def __str__(self):
        string = self.src.name
        string += " - "
        string += self.dst.name
        return string
	
class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255		
		
u = Vertex(c=VertexColor.WHITE, d1=1, d2=22, name = 'u')
v = Vertex(c=VertexColor.GRAY, p=u, d1=33, d2=4, name = 'v')



def initializeSingleSource(G, s):
    for i in G:
        i.d = math.inf
        i.p = None
    s[0].d = 0

def relax(u, v, w):
    for i in range(len(w)):
        if((w[i].src == u) & (w[i].dst == v)):
            wt = w[i].wt
            break

    if(v.d > u.d + wt):
        v.d = u.d + wt
        v.p = u

def dijkstra(G, w, s):
    initializeSingleSource(G, s)
    ls = []
    Q = G
    while(len(Q) > 0):
        u = extractMin(Q)
        for i in u.d1:
            relax(u, i, w)
    print("Dijkstra completed")

def extractMin(ls):
    min = math.inf
    node = None
    for i in ls:
        if i.d < min:
            min = i.d
            node = i
    ls.remove(node)
    return node

def printPath(ls, start):
    for i in ls:
        print("Starting with: " + i.name)
        while((i != start) & (i != None)):
            print(i.name)
            i = i.p
        if(i == start):
            print(i.name)
        print()

def randomGen():
    n_elem = random.choice(range(10))
    vortexes = []
    edges = []
    for i in range(n_elem):
        nomen = random.choice(string.ascii_letters)
        vortexes.append(Vertex(name = nomen, d1 = [], d2 = []))

    for i in range(n_elem*10):
        src = random.choice(vortexes)
        dst = random.choice(vortexes)
        k = 0
        if(src != dst):
            for k in range(len(edges)):
                if((edges[k].src == src) & (edges[k].dst == dst)):
                    break
            if (k == len(edges)):
                wt = random.choice(range(100))
                edges.append(Edge(src, dst, wt))
                src.d1.append(dst)
                src.d2.append(wt)

    print(edges)
    print(vortexes)
    return(vortexes, edges)
    
s = Vertex(name = 's')
t = Vertex(name = 't')
x = Vertex(name = 'x')
y = Vertex(name = 'y')
z = Vertex(name = 'z')

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

vortices = [s, t, x, y, z]

for i in vortices:
    print(i)

dijkstra(vortices, edges, [s])

vortices = [s, t, x, y, z]
printPath(vortices, s)

randomGen()