from Graph import *
import math

def MakeGraph():
    a = Vortex(name = 'a')
    b = Vortex(name = 'b')
    c = Vortex(name = 'c')
    d = Vortex(name = 'd')
    e = Vortex(name = 'e')
    f = Vortex(name = 'f')
    g = Vortex(name = 'g')
    
    vortices  = [a, b, c, d, e, f, g]

    ab = Edge(src = a, dst = b, weight = 8)
    ac = Edge(src = a, dst = c, weight = 6)
    bd = Edge(src = b, dst = d, weight = 10)
    cd = Edge(src = c, dst = d, weight = 15)
    ce = Edge(src = c, dst = e, weight = 9)
    de = Edge(src = d, dst = e, weight = 14)
    df = Edge(src = d, dst = f, weight = 4)
    ef = Edge(src = e, dst = f, weight = 13)
    eg = Edge(src = e, dst = g, weight = 17)
    fg = Edge(src = f, dst = g, weight = 7)

    edges = [ab, ac, bd, cd, ce, de, df, ef, eg, fg]

    graph = Graph(vortices = vortices, edges = edges)
    
    return graph

def GetInDegrees(graph):
    retList = []
    for i in graph.vortices:
        cnt = 0
        for j in range(len(graph.edges)):
            if(graph.edges[j].dst == i):
                cnt += 1
        retList.append(cnt)

    return retList

def GetOutDegrees(graph):
    retList = []
    for i in graph.vortices:
        cnt = 0
        for j in range(len(graph.edges)):
            if(graph.edges[j].src == i):
                cnt += 1
        retList.append(cnt)

    return retList

def InitializeSingleSource(graph, s):
    for i in graph.vortices:
        i.dist = math.inf
        i.parent = None
    s.dist = 0

def Relax(u, v, w):
    if (v.dist > u.dist + w.weight):
        v.dist = u.dist + w.weight
        v.parent = u

def ExtractMin(Q):
    min = math.inf
    node = None
    for i in Q:
        if i.dist <= min:
            min = i.dist
            node = i
    Q.remove(node)
    return node

def ShortestPath(graph, begin, end):
    InitializeSingleSource(graph, graph.vortices[0])
    for i in graph.vortices:
        for j in graph.edges:
            if i == j.src:
                Relax(j.src, j.dst, j)

    node = Vortex()

    for k in graph.vortices:
        if k == end:
            node = k
            break

    pathList = [node.name]
    pathDist = node.dist

    while (node != begin) & (node.parent != None):
        node = node.parent
        pathList.append(node.name)

    pathList.reverse()

    return (pathList, pathDist)

def UpdateEdge(graph, begin, end, weight):
    for i in graph.edges:
        if((i.src == begin) & (i.dst == end)):
            i.weight = weight
            return
    graph.edges.append(Edge(src = begin, dst = end, weight = weight))

def NewShortestPath():
    return ShortestPath(graph, graph.vortices[0], graph.vortices[6])


graph = Graph()
graph = MakeGraph()
inList = GetInDegrees(graph)
outList = GetOutDegrees(graph)
pathList = ShortestPath(graph, graph.vortices[0], graph.vortices[6])

print("In degrees:")
print(inList)
print()
print("Out degrees:")
print(outList)
print()
print("Path list from A to G")
print(pathList[0], "Distance:", pathList[1])

UpdateEdge(graph, graph.vortices[1], graph.vortices[2], -6)
newPath = NewShortestPath()
print()
print("New path list from A to G")
print(newPath[0], "Distance:", newPath[1])