class Node(object):
    def __init__(self,value):
           self.value = value
           self.left = None
           self.right = None


class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)
    
    def print_tree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        else:
            return print("Traversal type not supported.")
    
    def preorder_print(self,start,traversal):
        """Root > Left > Right"""
        if start:
            traversal += (str(start.value) +"-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
        
        
tree = BinaryTree(1) # initial value of the root
tree.root.left = Node(2)
# So far:
#   1
#  /
# 2
tree.root.right = Node(3)
# So far:
#   1
#  / \
# 2   3
tree.root.left.left = Node(4)
# So far:
#      1
#     / \
#    2   3
#   /
#  4
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
# So far:
#       1
#     /   \
#    2     3
#   / \   / \
#  4   5 6   7


print(tree.print_tree("preorder"))
