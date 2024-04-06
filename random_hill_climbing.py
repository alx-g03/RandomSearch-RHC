import random
import time


def evaluate_solution(solution, objects, max_weight):
    total_value = 0
    total_weight = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_value += objects[i][1]
            total_weight += objects[i][2]
    if total_weight > max_weight:
        return 0, 0
    else:
        return total_value, total_weight


def random_neighbors(solution, num_neighbors):
    neighbors = []
    for _ in range(num_neighbors):
        neighbor = solution[:]
        index = random.randint(0, len(solution) - 1)
        neighbor[index] = 1 - neighbor[index]
        neighbors.append(neighbor)
    return neighbors


def random_hill_climbing(objects, max_weight, max_iterations, num_neighbors):
    start_time = time.perf_counter()

    current_solution = [random.randint(0, 1) for _ in range(len(objects))]
    current_value, current_weight = evaluate_solution(current_solution, objects, max_weight)
    best_solution = current_solution[:]
    best_value = current_value
    valid_values = [current_value] if current_weight <= max_weight else []

    for _ in range(max_iterations):
        neighbors = random_neighbors(current_solution, num_neighbors)
        for neighbor in neighbors:
            neighbor_value, neighbor_weight = evaluate_solution(neighbor, objects, max_weight)
            if neighbor_value > best_value:
                best_solution = neighbor[:]
                best_value = neighbor_value
            if neighbor_value > current_value and neighbor_weight <= max_weight:
                current_solution = neighbor[:]
                current_value = neighbor_value
                valid_values.append(current_value)

    end_time = time.perf_counter()
    exec_time = end_time - start_time

    valid_values_average = sum(valid_values) / len(valid_values)

    return best_solution, best_value, valid_values_average, exec_time
