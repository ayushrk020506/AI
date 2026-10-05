import heapq
print("Ayush R Kallingal\n1WN24CS057")
GOAL =  (1, 2, 3,
         8, 0, 4,
         7, 6, 5)


# Take initial state from user
print("Enter initial state:")

row1 = list(map(int, input("Row 1: ").split()))
row2 = list(map(int, input("Row 2: ").split()))
row3 = list(map(int, input("Row 3: ").split()))

START = tuple(row1 + row2 + row3)


def heuristic(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1

    return count


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def a_star(start):
    h = heuristic(start)

    pq = [(h, 0, start, [start])]
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current == GOAL:
            return path

        for neighbor in get_neighbors(current):

            if neighbor in visited:
                continue

            new_g = g + 1
            new_h = heuristic(neighbor)
            new_f = new_g + new_h

            heapq.heappush(
                pq,
                (new_f, new_g, neighbor, path + [neighbor])
            )

    return None


def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


solution = a_star(START)

print("Initial State:")
print_puzzle(START)

print("Goal State:")
print_puzzle(GOAL)

print("Solution:")

for step, state in enumerate(solution):
    g = step
    h = heuristic(state)
    f = g + h

    print("Step", step)
    print_puzzle(state)
    # print("g(n) =", g)
    # print("h(n) =", h)
    print("f(n) =", f)
    print()