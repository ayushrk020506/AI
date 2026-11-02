import random
import math

N = 8

def calculate_cost(board):
    cost = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                cost += 1
    return cost


def display_board(board):
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()


def simulated_annealing():
    # Initial configuration
    current = [0, 4, 2, 5, 7, 1, 6, 3]

    temperature = 1000
    cooling_rate = 0.99

    print("SIMULATED ANNEALING - 8 QUEENS PROBLEM")

    print("\nInitial State:", current)
    print("Initial Cost:", calculate_cost(current))

    while temperature > 0.01:

        current_cost = calculate_cost(current)

        if current_cost == 0:
            print("\nGoal State Reached!")
            break

        neighbor = current.copy()

        col = random.randint(0, N - 1)
        row = random.randint(0, N - 1)
        neighbor[col] = row

        neighbor_cost = calculate_cost(neighbor)
        delta = neighbor_cost - current_cost

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current = neighbor

        temperature *= cooling_rate

    if calculate_cost(current) == 0:
        print("\nFinal Solution:", current)
        print("Final Cost:", calculate_cost(current))

        print("\nFinal Chessboard:")
        display_board(current)
    else:
        print("\nGoal State Not Reached!")


simulated_annealing()