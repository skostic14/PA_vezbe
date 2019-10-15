from class_example import Data
from class_example import Node
from class_example import Tree
from class_example import random_list

d = Data(99, 2)
print(d.a1, d.a2)

l = Data(3, 5)
r = Data(4, 6)
x = Data(5, 7)
y = Data(6, 3)
z = Data(9, 11)

nl = Node(None, None, None, l)
nr = Node(None, None, None, r)
np = Node(None, None, None, d)
nx = Node(None, None, None, x)
ny = Node(None, None, None, y)
nz = Node(None, None, None, z)


t = Tree()
t.insert(np)



l1 = random_list(50)
nodes = []
for i in range(50):
    nodes.append(Node(None, None, None, Data(l1[i], 0)))

for i in range(50):
    t.insert(nodes[i])

l2 = l1[:]
l3 = []

print(t.tree_search(t.root, 8))
print(t.iterative_tree_search(t.root, 8))

t.delete(np)
t.inorder_walk(t.root, l3)


l2.sort()
print("List sort()\n", l2, "\n")
print("Inorder Walk\n", l3)