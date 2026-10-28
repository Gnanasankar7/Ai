from prgm1 import bfs, dfs, graph


start_node = 'A'
print("Breadth-First Search (BFS):")
print(bfs(graph, start_node))
print("\nDepth-First Search (DFS):")
print(dfs(graph, start_node))