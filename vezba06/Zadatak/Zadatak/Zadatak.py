from classes import Node
import math
import random

def GetHistogram(list):
    hist = dict()
    for i in range(len(list)):
        if list[i] in hist:
            hist[list[i]] += 1
        else:
            hist[list[i]] = 1
    return hist

def RemoveElem(list):
    list.pop(0)

def GetMinFreqElem(list):
    return list[0]

def PutElem(list, elem):
    list.append(elem)
    list.sort()

def MakeNewElem(list):
    tempNode = Node("cvor", list[0].freq + list[1].freq)
    list[0].parent = tempNode
    list[1].parent = tempNode
    tempNode.left = list[0]
    tempNode.right = list[1]
    list.pop(0)
    list.pop(0)
    list.append(tempNode)
    list.sort()


input5 = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']
dict = GetHistogram(input5)

#print(dict)
nodes = []

for i in range (len(dict)):
    temp = dict.popitem()
    nodes.append(Node(temp[0], temp[1]))

nodes.sort()

##for i in range (len(nodes)):
   ## print(nodes[i].freq, nodes[i].val)

while len(nodes) > 1:
    MakeNewElem(nodes)

##for i in range (len(nodes)):
    ##print(nodes[i].freq, nodes[i].val)

nodes[0].PrintTree()
str = ""
nodes[0].CodeLetter('a', str)
print(str)
