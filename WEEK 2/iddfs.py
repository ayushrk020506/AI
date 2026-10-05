# 8-Puzzle using Depth Limited Search
# 0 represents the blank space

CUTOFF = "CUTOFF"
FAILURE = "FAILURE"
print("Ayush R Kallingal\n1WN24CS057")

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_successors(state):
    successors = []

    x, y = find_blank(state)

    # Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:

            new_state = [row[:] for row in state]

            # Move blank
            new_state[x][y], new_state[nx][ny] = \
                new_state[nx][ny], new_state[x][y]

            successors.append(new_state)

    return successors


def state_to_tuple(state):
    return tuple(tuple(row) for row in state)


def DLS(node, goal, limit, path, visited):

    # Goal found
    if node == goal:
        return path

    # Depth limit reached
    if limit == 0:
        return CUTOFF

    cutoff_occurred = False

    for child in get_successors(node):

        child_tuple = state_to_tuple(child)

        # Avoid repeating states in current path
        if child_tuple in visited:
            continue

        visited.add(child_tuple)
        path.append(child)

        result = DLS(
            child,
            goal,
            limit - 1,
            path,
            visited
        )

        # Solution found
        if result != CUTOFF and result != FAILURE:
            return result

        # Some node reached the depth limit
        if result == CUTOFF:
            cutoff_occurred = True

        path.pop()
        visited.remove(child_tuple)

    if cutoff_occurred:
        return CUTOFF

    return FAILURE


def IDDFS(start, goal, limit):

    path = [start]

    visited = {state_to_tuple(start)}

    return DLS(
        start,
        goal,
        limit,
        path,
        visited
    )


# ---------------------------------------
# INPUT INITIAL STATE
# ---------------------------------------

print("Enter Initial State:")
print("Use 0 for the blank space")

initial = []

for i in range(3):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    initial.append(row)


# ---------------------------------------
# INPUT LIMIT
# ---------------------------------------

limit = int(input("\nEnter depth limit: "))


# ---------------------------------------
# GOAL STATE
# ---------------------------------------

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


# ---------------------------------------
# START SEARCH
# ---------------------------------------

result = IDDFS(initial, goal, limit)


# ---------------------------------------
# OUTPUT
# ---------------------------------------

if result == CUTOFF:

    print("\nCUTOFF")
    print("Goal was not found within the given depth limit.")

elif result == FAILURE:

    print("\nFAILURE")
    print("No solution exists within the given depth limit.")

else:

    path = result

    path_cost = len(path) - 1

    print("\nGoal Found!")

    print("\nSolution Path:")

    for state in path:

        for row in state:
            print(row)

        print()

    print("Path Cost:", path_cost)