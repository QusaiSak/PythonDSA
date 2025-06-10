from collections import deque
from init import Node

# left , root , right
def in_order_dfs(root):
    if root is None:
        return
    in_order_dfs(root.left)
    print(root.data, end=' ')
    in_order_dfs(root.right)
    
# root , left , right
def pre_order_dfs(root):
    if root is None:
        return 
    print(root.data , end=' ')
    pre_order_dfs(root.left)
    pre_order_dfs(root.right)

# left , right , root
def post_order_dfs(root):
    if root is None:
        return
    post_order_dfs(root.left)
    post_order_dfs(root.right)
    print(root.data, end=' ')
    
# level order ==> BFS
def bfs(root):
    if root is None:
        return 
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.data, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def zigzagBFS(root):
    if root is None:
            return []
    res = []
    q = deque([root])
    reverse = False
    while q:
        level = []
        level_queue = len(q)
        for _ in range(level_queue):
            curr = q.popleft()
            level.append(curr.data)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        if reverse:
            level.reverse()
        reverse = not reverse
        res.append(level)
    return res

# Morris Traversal 
def morris_traversal(root):
    curr = root
    result = []
    while curr is not None:
        if curr.left is None:
            result.append(curr.data)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right is not None and pre.right!= curr:
                pre = pre.right
                
            if pre.right is None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                result.append(curr.data)
                curr = curr.right
    return result


if __name__ == "__main__":
    root = Node(1);
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7) 
    
    print("Binary Tree Traversal:")
    print("In-order DFS:")
    in_order_dfs(root)
    print("\nPre-order DFS:")
    pre_order_dfs(root)
    print("\nPost-order DFS:")
    post_order_dfs(root)
    print("\nBFS:")
    bfs(root)
    print("\nZigzag BFS:")
    print(zigzagBFS(root))
    
    