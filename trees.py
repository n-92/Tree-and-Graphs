"""
Aung Naing Oo
A quick and dirty review on trees and related algorithms
/* In-Order Traversal 
* Visit (print) the left branch, then the current node, and finally, the right branch. 
*/

/* Pre-Order Traversal
* Visit the current node (print), before its left and right child nodes. 
*/

/* Post-Order Traversal of a Tree is also a Depth First Search
* Visit the current node (print), after its left and right child nodes.
*/

/*Breadth First Search
*Visit the current node, and its left and right neighbours before visiting
*the neighbours of its left and right neighbours and so on level by level
*/
"""



class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data == None:
            return None

        if data <= self.data:
            if self.left is None:
                self.left= Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data

    def inorder_print(self):
      if self.left:
         self.left.inorder_print()
      print(self.data),
      if self.right:
         self.right.inorder_print()

    def postorder_print(self):
      if self.left:
         self.left.postorder_print()
      if self.right:
         self.right.postorder_print()
      print(self.data)

    def preorder_print(self):
      print(self.data)
      if self.left:
         self.left.preorder_print()
      if self.right:
         self.right.preorder_print()
      

def bfs(root):
    queue = []
    queue.append(root)
    while len(queue)>0:
        x = queue.pop(0)
        print(x.data)
        if x.left:
            queue.append(x.left)
        if x.right:
            queue.append(x.right)
        
            

root = Node(8)
root.insert(4)
root.insert(10)
root.insert(2)
root.insert(6)
root.insert(20)
print("In Order Traversal of a Tree")
root.inorder_print()

print("Post Order Traversal of a Tree")
root.postorder_print()

print("Pre OrderTraversal of a Tree")
root.preorder_print()


print("Breadth First Search of a Tree")
bfs(root)
