import random

class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self, p = None, l = None, r = None, d = None):
        """
        Node constructor 
        @param A node data object
        """
        self.parent = p
        self.left = l
        self.right = r
        self.data = d

class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.data.a1 < x.data.a1:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.data.a1 < y.data.a1:
            y.left = z
        else:
            y.right = z

    def delete(self, z):
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            if y.parent != z:
              self.transplant(y, y.right)
              y.right = z.right
              y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    def inorder_walk(self, x, list):
        if x != None:
            self.inorder_walk(x.left, list)
            list.append(x.data.a1)
            print(x.data.a1)
            self.inorder_walk(x.right, list)
        

    def tree_search(self, x, k):
        if x == None or k == x.data.a1:
            return x
        if k < x.data.a1:
            return self.tree_search(x.left, k)
        else:
            return self.tree_search(x.right, k)

    def iterative_tree_search(self, x, k):
        while x!=None and k != x.data.a1:
            if k < x.data.a1:
                x = x.left
            else:
                x = x.right
        return x

    def tree_minimum(self, x):
        while x.left != None:
            x = x.left
        return x

    def tree_maximum(self, x):
        while x.right != None:
            x = x.right
        return x

    def tree_successor(self, x):
        if x.right != None:
            return self.tree_minimum
        y = x.parent
        while y!=None and x == y.right:
            x = y
            y = y.parent
        return y
    
def random_list(max):
    list = []
    for i in range(max):
        list.append(random.choice(range(max)))
    return list