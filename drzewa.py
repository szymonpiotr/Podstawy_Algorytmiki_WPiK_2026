class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(10)
root.right.right.right = Node(11)

def is_element(root, element):
   if root.left == None and root.right == None:
      return element == root.data
   else:
      return (is_element(root.left, element) or is_element(root.right, element)) or root.data == element

print(is_element(root, 1))

#1. Zdefniuj funkcję, która dla danego drzewa zwróci ilość węzłów. 



 #2. Sprawdź, czy drzewo jest w równowadze (globalnie).  


 #3. Sprawdź, czy drzewo jest w równowadze (lokalnie).   

