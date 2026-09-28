print("Ayush R Kallingal\n1WN24CS057")
print("Enter initial state (use 0 for blank):")
initial = tuple(map(int, input().split()))

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


def distance(state):
    total = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])

            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(goal_pos, 3)

            total += abs(r1 - r2) + abs(c1 - c2)

    return total


def generate_moves(state):
    moves = []

    blank = state.index(0)
    row, col = divmod(blank, 3)

    if row > 0:
        new_state = list(state)
        new_state[blank], new_state[blank - 3] = \
            new_state[blank - 3], new_state[blank]
        moves.append(tuple(new_state))

    if row < 2:
        new_state = list(state)
        new_state[blank], new_state[blank + 3] = \
            new_state[blank + 3], new_state[blank]
        moves.append(tuple(new_state))

    if col > 0:
        new_state = list(state)
        new_state[blank], new_state[blank - 1] = \
            new_state[blank - 1], new_state[blank]
        moves.append(tuple(new_state))

    if col < 2:
        new_state = list(state)
        new_state[blank], new_state[blank + 1] = \
            new_state[blank + 1], new_state[blank]
        moves.append(tuple(new_state))

    return moves


def dfs(initial, goal):

    stack = [(initial, [initial])]

    visited = set()
    visited.add(initial)

    while stack:

        state, path = stack.pop()

        if state == goal:

            print("\nSolution found!")
            print("Path:\n")

            for i, s in enumerate(path):
                print("Step", i)
                display(s)

            print("Path Cost:", len(path) - 1)
            return

        moves = generate_moves(state)

        moves.sort(key=distance, reverse=True)

        for new_state in moves:

            if new_state not in visited:

                stack.append((new_state, path + [new_state]))
                visited.add(new_state)

    print("No solution")


dfs(initial, goal)