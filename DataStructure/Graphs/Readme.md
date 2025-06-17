# 📊 Difference Between Graph and Tree

| Feature               | Graph                                                                 | Tree                                                                       |
|-----------------------|-----------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Definition**         | A collection of nodes (vertices) and edges, where edges connect nodes arbitrarily. | A hierarchical structure with a single root node and parent-child relationships. |
| **Structure**          | Can have cycles and disconnected components.                         | No cycles; always connected with exactly one path between any two nodes.  |
| **Root Node**          | No root node; any node can be a starting point.                      | Has a designated root node with no parent.                                |
| **Node Relationship**  | Arbitrary connections between nodes.                                 | Each node (except the root) has exactly one parent.                       |
| **Edges**              | Can have many edges; possibly more than `n-1` for `n` nodes.          | Always has exactly `n-1` edges for `n` nodes.                             |
| **Traversal Complexity**| May require cycle detection and handling disconnected components.   | Straightforward traversal using tree traversal methods (DFS, BFS, etc).   |
| **Applications**       | Used in social networks, maps, web pages, network routing, etc.      | Used in file systems, XML/HTML DOM, family trees, org charts, etc.       |
| **Examples**           | Facebook friends graph, Google Maps, Internet topology.              | Windows File Explorer, HTML DOM Tree, Family genealogy tree.             |

> ✅ **Note:** A Tree is a special type of Graph — specifically, a connected, acyclic graph with a root.