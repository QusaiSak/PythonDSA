def add_edge(mat,i,j):
    mat[i][j] = 1
    mat[j][i] = 1

def display(mat):
    for row in mat:
        print(" ".join(str(x) for x in row))

V = 4  # Number of vertices
mat = [[0] * V for _ in range(V)]  

    # Add edges to the graph
add_edge(mat, 0, 1)
add_edge(mat, 0, 2)
add_edge(mat, 1, 2)
add_edge(mat, 2, 3)

# Display the adjacency matrix
print("Adjacency Matrix:")
display(mat)