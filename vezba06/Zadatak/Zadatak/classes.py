class Node:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
        self.parent = None
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.freq < other.freq:
            return True
        return False

    def PrintTree(self):
        if(self.val == "cvor"):
            self.left.PrintTree()
            self.right.PrintTree()
        else:
            print(self.val, self.freq)

    def CodeLetter(self, val, str):
        if self != None:
            self.left.CodeLetter(val, str)
            
            self.right.CodeLetter(val, str)
