from prgm4 import hill_climbing

start_point = 0
best_x, best_value = hill_climbing(start_point)
print("\nBest Solution Found")
print("Optimal x =", best_x)
print("Maximum Value =", best_value)