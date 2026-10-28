from prgm3 import astar, graph

start = 'A'
goal = 'G'
path = astar(start, goal)
cost = sum(
	next(edge_cost for neighbor, edge_cost in graph[current] if neighbor == following)
	for current, following in zip(path, path[1:])
)
print("-------------------------")
print("Optimal Path :", " -> ".join(path))
print("Total Cost :", cost)