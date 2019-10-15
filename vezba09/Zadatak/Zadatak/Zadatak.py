from vertex_example import *
import math

def bfs(G,s):
    for i in G:
        if(i != s):
            i.c = VertexColor.WHITE
            i.d2 = math.inf
            i.p = None
    q = []
    s.c = VertexColor.GRAY
    s.d2 = 0
    s.p = None
    q.append(s)

    while (len(q) > 0):
        u = q.pop()
        for i in u.d1:
            if (i.c == VertexColor.WHITE):
                i.c = VertexColor.GRAY
                i.d2 = u.d2+1
                i.p = u
                q.append(i)
        u.c = VertexColor.BLACK

def printPath(G, s, v):
    if(v == s):
        print(s.n)
    elif(v.p == None):
        print("No path from", s.n, "to", v.n, "exists!")
    else:
        printPath(G, s, v.p)
        print(v.n)

def dfs(G):
    print("DFS")
    for node in G:
        node.c = VertexColor.WHITE
        node.p = None
    time = Time()
    for node in G:
        if(node.c == VertexColor.WHITE):
            dfsVisit(G, node, time)

def dfsVisit(G, u, time):
    time.t +=1
    u.d2 = time
    u.c = VertexColor.GRAY
    for node in u.d1:
        if(node.c == VertexColor.WHITE):
            node.p = u
            dfsVisit(G, node, time)
    u.c = VertexColor.BLACK
    time.t+=1
    u.f = time.t
    print("Vertex:", u.n, "Finish time:", u.f)

def topologicalSort(G):
    dfs(G)
    G.sort(reverse = True)
    

vertex = []

for i in range(6):
    vertex.append(Vertex(c = VertexColor.WHITE, n = i+1))

v0_list = []
v0_list.append(vertex[1])
v0_list.append(vertex[3])
vertex[0].d1 = v0_list

v1_list = []
v1_list.append(vertex[4])
vertex[1].d1 = v1_list

v2_list = []
v2_list.append(vertex[5])
v2_list.append(vertex[4])
vertex[2].d1 = v2_list

v3_list = []
v3_list.append(vertex[1])
vertex[3].d1 = v3_list

v4_list = []
v4_list.append(vertex[3])
vertex[4].d1 = v4_list

v5_list = []
v5_list.append(vertex[5])
vertex[5].d1 = v5_list

for i in range(6):
    print("Neighbors of Vertex:", i+1)
    for j in range(len(vertex[i].d1)):
        print(vertex[i].d1[j].n)
    print()

bfs(vertex, vertex[0])
printPath(vertex, vertex[0], vertex[4])

print()
print()
dfs(vertex)

clothes = []
undershorts = Vertex(n = "undershorts")
socks = Vertex(n = "socks")
pants = Vertex(n = "pants")
shoes = Vertex(n = "shoes")
watch = Vertex(n = "watch")
belt = Vertex(n = "belt")
shirt = Vertex(n = "shirt")
tie = Vertex(n = "tie")
jacket = Vertex(n = "jacket")

undershorts.d1 = [pants, shoes]
socks.d1 = [shoes]
pants.d1 = [belt, shoes]
shirt.d1 = [belt, tie]
belt.d1 = [jacket]
tie.d1 = [jacket]
watch.d1 = []
jacket.d1 = []
shoes.d1 = []

clothes.append(undershorts)
clothes.append(socks)
clothes.append(pants)
clothes.append(shoes)
clothes.append(watch)
clothes.append(belt)
clothes.append(shirt)
clothes.append(tie)
clothes.append(jacket)

print()
print()

print("Topological Sort")

topologicalSort(clothes)
print()
for i in clothes:
    print(i.n)
