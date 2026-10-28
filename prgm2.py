from collections import deque


goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
]


def to_tuple(state):
    return tuple(tuple(row) for row in state)


def find_blank(state):
    for row_index in range(3):
        for column_index in range(3):
            if state[row_index][column_index] == 0:
                return row_index, column_index
    raise ValueError("Puzzle state has no blank tile")


def get_neighbors(state):
    neighbors = []
    blank_row, blank_column = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for row_delta, column_delta in moves:
        new_row = blank_row + row_delta
        new_column = blank_column + column_delta
        if 0 <= new_row < 3 and 0 <= new_column < 3:
            new_state = [row[:] for row in state]
            new_state[blank_row][blank_column], new_state[new_row][new_column] = (
                new_state[new_row][new_column],
                new_state[blank_row][blank_column],
            )
            neighbors.append(new_state)

    return neighbors


def solve_puzzle(start_state):
    queue = deque([(start_state, [])])
    visited = {to_tuple(start_state)}

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path + [current_state]

        for neighbor in get_neighbors(current_state):
            neighbor_key = to_tuple(neighbor)
            if neighbor_key not in visited:
                visited.add(neighbor_key)
                queue.append((neighbor, path + [current_state]))

    return None


def print_state(state):
    for row in state:
        print(row)
    print()