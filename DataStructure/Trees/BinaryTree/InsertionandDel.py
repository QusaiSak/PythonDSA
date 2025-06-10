from collections import deque
from init import Node
from printTree import print_tree

# Insertion
def insert_binary_tree(root,data):
    if root is None:
        return Node(data)
    q = deque([root])
    
    while q:
        current = q.popleft()
        if current.left is None:
            current.left = Node(data)
            break
        else:
            q.append(current.left)
        
        if current.right is None:
            current.right = Node(data)
            break
        else:
            q.append(current.right)
    return root


# Deletion
def delete_binary_tree(root,data):
    if root is None:
        return None
    q = deque([root])
    target = None
    while q:
        current = q.popleft()
        if current.data == data:
            target = current
            break
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
        
    if target is None:
        return root
        
    last_node = None
    last_parent = None
    q = deque([(root,None)])
    while q:
        current,parent = q.popleft()
        last_node = current
        last_parent = parent
        if current.left:
            q.append((current.left, current))
        if current.right:
            q.append((current.right, current))
    target.data = last_node.data
    if last_parent:
        if last_parent.left == last_node:
            last_parent.left = None
        else:
            last_parent.right = None    
    else:
        return None
    return root     
            

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("Binary Tree Before Insertion:")
    print_tree(root)
    root = insert_binary_tree(root, 8)
    print("\nBinary Tree After Insertion:")
    print_tree(root)
    root = delete_binary_tree(root, 3)
    print("\nBinary Tree After Deletion:")
    print_tree(root)
