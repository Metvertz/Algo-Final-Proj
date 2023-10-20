import itertools
import time

# Nearest Neighbor Method
def nearest_neighbor(dist_matrix, start=0):
    num_cities = len(dist_matrix)
    unvisited = set(range(num_cities))
    current_city = start
    tour = [current_city]
    unvisited.remove(current_city)

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start)  # Return to the start city
    return tour

# Brute Force Method
def brute_force_tsp(dist_matrix):
    num_cities = len(dist_matrix)
    shortest_tour = None
    shortest_distance = float('inf')

    for tour in itertools.permutations(range(1, num_cities)):  
        tour = [0] + list(tour) + [0]  
        distance = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(num_cities))
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_tour = tour

    return shortest_tour

def compute_tour_length(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

if __name__ == "__main__":
    dist_matrix = [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ]

    start_time = time.time()
    brute_tour = brute_force_tsp(dist_matrix)
    brute_time = time.time() - start_time

    print("Brute Force Tour:", brute_tour)
    print("Brute Force Tour Length:", compute_tour_length(brute_tour, dist_matrix))
    print("Brute Force Time:", brute_time, "seconds\n")

    start_time = time.time()
    nn_tour = nearest_neighbor(dist_matrix)
    nn_time = time.time() - start_time

    print("Nearest Neighbor Tour:", nn_tour)
    print("Nearest Neighbor Tour Length:", compute_tour_length(nn_tour, dist_matrix))
    print("Nearest Neighbor Time:", nn_time, "seconds")
