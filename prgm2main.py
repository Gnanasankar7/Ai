from prgm2 import print_state, solve_puzzle


start_state = [
    [1, 0, 3],
    [4, 2, 6],
    [7, 5, 8],
]

solution = solve_puzzle(start_state)
if solution:
    print("Solution Found!")
    print("Number of moves:", len(solution) - 1)
    for step, state in enumerate(solution):
        print("\nStep", step)
        print_state(state)
else:
    print("No solution found.")