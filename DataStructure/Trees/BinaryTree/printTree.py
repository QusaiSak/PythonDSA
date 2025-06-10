def print_tree(root, level=0):
    if root != None:
        print_tree(root.left, level + 1)
        print(" " * 4 * level + "-> " + str(root.data))
        print_tree(root.right, level + 1)
