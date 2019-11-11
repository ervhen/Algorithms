#Ervin Hennrich
#11/27/18 for compsci 3130
#Program that creates a Binary Search Tree and functions to insert, delete, search and print (Inorder,preorder and postorder)
#Uses two classes, BST and node. The BST keeps track of the root, which is a node. The node class keeps the key value, and
#which nodes are to the right/left as well as the parent of the node. My functions are similar to the ones from the handout,
#except I used recurrsion.

class node:
    def __init__(self, parent=None, val=None):
        self.key = val
        self.right = None
        self.left = None
        self.parent = parent

    def __del__(self):
        self.key = None
        self.right = None
        self.left = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None

def Insert(start, val):
    if start.key is None:
        start.key = val
    else:
        if int(start.key) > val:
            if start.left is None:
                start.left = node(start, val)
            else:
                Insert(start.left, val)
        else:
            if start.right is None:
                start.right = node(start, val)
            else:
                Insert(start.right, val)

#The delete function, first finds the postition of the value to be deleted then changes the values.
def Finder(tree, start, val):
    if start.key is None:
        print("The Tree is empty")
    else:
        #if/else checks which side to go down
        if int(start.key) > val: #if val is down left - root can never be in here
            if int(start.key) == val:
                if start.left is None or start.right is None:
                    y = start
                else:
                    y = Successor(start)
                if y.left is not None:
                    x = y.left
                else:
                    x = y.right
                if x is not None:
                    x.parent = y.parent
                elif y is y.parent.left:
                    y.parent.left = x
                else:
                    y.parent.right = x
                return
            else:
                Finder(tree, start.left, val)
        else: #val is right or the root
            if int(start.key) == val: 
                if start.left is None or start.right is None:
                    y = start
                else:
                    y = Successor(start)
                if y.left is not None:
                    x = y.left
                else:
                    x = y.right
                if x is not None:
                    x.parent = y.parent
                if start.parent is None:
                    hold = tree.root
                    tree.root.key = y.key
                    y.parent.left = None
                elif y is y.parent.left:
                    y.parent.left = None
                    start.key = y.key
                    y.key = None
                else:
                    y.parent.right = x
                return
            else:
                Finder(tree, start.right, val)


def Successor(start):
    if start.right is not None:
        return Tree_Min(start.right)
    y = start.parent
    while y is not None and start is y.right:
        start = y
        y = y.parent
    return y

def Tree_Min(start):
    while start.left is not None:
        start=start.left
    return start


def Search(start, val):
    if start is None:
        print("NIL")
    else:
        if int(start.key) > val:
            print(start.key, " ", end='')
            if start.key == val:
                return
            Search(start.left, val)
        else:
            print(start.key, " ", end='')
            if start.key == val:
                return
            Search(start.right, val)


def Tree_Print(inner):
    if inner is None:
        print("The tree is empty")
        return
    print("Inorder: ")
    Inorder(inner)
    print()
    print("Preorder: ")
    Preorder(inner)
    print()
    print("Postorder: ")
    Postorder(inner)


def Inorder(inner):
    if inner.left is not None:
        Inorder(inner.left)
    print(inner.key," ", end='')
    if inner.right is not None:
        Inorder(inner.right)

def Preorder(inner):
    print(inner.key, " ", end='')
    if inner.left is not None:
        Preorder(inner.left)
    if inner.right is not None:
        Preorder(inner.right)
        

def Postorder(inner):
    if inner.left is not None:
        Postorder(inner.left)
    if inner.right is not None:
        Postorder(inner.right)
    print(inner.key," ", end='')
    

Startarr = [30, 10, 45, 38, 20, 50, 25, 33, 8, 12]
tree = BST()
tree.root = node()
thein = 0
while thein is not 6:
    thein = int(input("\n1)Insert 2)Insert the array 3)Delete 4)Search 5)Print 6)Quit\n"))
    if thein == 1:
        val = int(input("What should I Insert?\n"))
        Insert(tree.root, val)
    if thein == 2:
        for i in range(len(Startarr)):
            Insert(tree.root, Startarr[i])
    if thein == 3:
        val = int(input("What should I Delete?\n"))
        Finder(tree, tree.root, val)
    if thein == 4:
        val = int(input("What should I Search for?\n"))
        Search(tree.root, val)
    if thein == 5:
        Tree_Print(tree.root)
    if thein == 6:
        break
