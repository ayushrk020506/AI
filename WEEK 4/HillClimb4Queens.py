
def calculate_cost(state):
    cost = 0

    # Check every pair of queens
    for i in range(4):
        for j in range(i + 1, 4):

            # Same row or same diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                cost += 1

    return cost


def hill_climbing(state):
    swaps = 0

    print("\nInitial State:", state)
    print("Initial Cost:", calculate_cost(state))

    while calculate_cost(state) != 0:

        current_cost = calculate_cost(state)
        neighbors = []

        # Generate all neighboring states
        for i in range(4):
            for j in range(i + 1, 4):

                neighbor = state.copy()

                # Swap the row positions of two queens
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

                neighbor_cost = calculate_cost(neighbor)

                neighbors.append((neighbor_cost, i, j, neighbor))

        # Select the neighbor with minimum cost
        # Tie-breaking: smallest subscript pair
        neighbors.sort(key=lambda x: (x[0], x[1], x[2]))

        best_cost, i, j, best_neighbor = neighbors[0]

        print("\nCurrent State:", state)
        print("Current Cost:", current_cost)

        print("Neighbor Costs:")
        for cost, a, b, neighbor in neighbors:
            print(f"Swap (x{a}, x{b}) -> {neighbor}, Cost = {cost}")

        # Check whether an improvement is possible
        if best_cost >= current_cost:
            print("\nHill Climbing terminated at a local minimum.")
            break

        # Perform the selected swap
        state = best_neighbor
        swaps += 1

        print("Selected Swap: (x{}, x{})".format(i, j))
        print("Next State:", state)
        print("Next Cost:", best_cost)
        print("Number of Swaps:", swaps)

    print("\n----- FINAL RESULT -----")
    print("Final State:", state)
    print("Final Cost:", calculate_cost(state))
    print("Total Swaps Performed:", swaps)

    if calculate_cost(state) == 0:
        print("Goal State Reached!")


# Input initial state
print("Enter initial row positions of queens (0 to 3):")

x0 = int(input("Enter x0: "))
x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
x3 = int(input("Enter x3: "))

initial_state = [x0, x1, x2, x3]

# Validate input
if sorted(initial_state) != [0, 1, 2, 3]:
    print("Invalid input! Enter each value from 0 to 3 exactly once.")
else:
    hill_climbing(initial_state)
