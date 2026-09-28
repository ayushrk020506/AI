# 8-Puzzle using DFS

# Input initial state
print("Enter initial state (use 0 for blank):")
initial = tuple(map(int, input().split()))

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Display puzzle
def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# Calculate Manhattan distance
def distance(state):
    total = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])

            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(goal_pos, 3)

            total += abs(r1 - r2) + abs(c1 - c2)

    return total


# Generate possible moves
def generate_moves(state):
    moves = []

    blank = state.index(0)
    row, col = divmod(blank, 3)

    # Up
    if row > 0:
        new_state = list(state)
        new_state[blank], new_state[blank - 3] = \
            new_state[blank - 3], new_state[blank]
        moves.append(tuple(new_state))

    # Down
    if row < 2:
        new_state = list(state)
        new_state[blank], new_state[blank + 3] = \
            new_state[blank + 3], new_state[blank]
        moves.append(tuple(new_state))

    # Left
    if col > 0:
        new_state = list(state)
        new_state[blank], new_state[blank - 1] = \
            new_state[blank - 1], new_state[blank]
        moves.append(tuple(new_state))

    # Right
    if col < 2:
        new_state = list(state)
        new_state[blank], new_state[blank + 1] = \
            new_state[blank + 1], new_state[blank]
        moves.append(tuple(new_state))

    return moves


# DFS
def dfs(initial, goal):

    # STACK
    stack = [(initial, [initial])]

    # Visited states
    visited = set()
    visited.add(initial)

    while stack:

        # Remove top state from STACK
        state, path = stack.pop()

        # Check goal
        if state == goal:

            print("\nSolution found!")
            print("Path:\n")

            for i, s in enumerate(path):
                print("Step", i)
                display(s)

            print("Path Cost:", len(path) - 1)
            return

        # Generate possible moves
        moves = generate_moves(state)

        # Sort moves according to distance from goal
        moves.sort(key=distance, reverse=True)

        # Add states to STACK
        for new_state in moves:

            if new_state not in visited:

                stack.append((new_state, path + [new_state]))
                visited.add(new_state)

    print("No solution")


# Start DFS
dfs(initial, goal)