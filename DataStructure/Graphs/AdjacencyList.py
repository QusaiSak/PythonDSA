def add_edge(graph,i,j):
    graph[i].append(j)
    graph[j].append(i)

def display(graph):
    for i in range(len(graph)):
        print(f"{i}: {' '.join(str(x) for x in graph[i])}")

V = 4
graph = [[] for _ in range(V)]  # Initialize an empty adjacency list
# Add edges to the graph
add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 1, 2)
add_edge(graph, 2, 3)

# Display the adjacency list
print("Adjacency List:")
display(graph)