import sys
import random  # Import the random module to generate random numbers

class GeneticAlgorithmTSP:
    def __init__(self, coordinates, distances, num_points, population_size=50, generations=1000, mutation_rate=0.2):
        """
        Initializes the GeneticAlgorithmTSP class.
        
        Args:
            coordinates (list of tuples): Coordinates of cities.
            distances (list of lists): Distances between cities.
            num_points (int): Number of cities.
            population_size (int): Size of the population in each generation.
            generations (int): Number of generations.
            mutation_rate (float): Probability of mutation in an individual.
        """
        self.coordinates = coordinates
        self.distances = distances
        self.num_points = num_points
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate        
        self.population = self.initialize_population()
    
    def initialize_population(self):
        """
        Initializes the population with random permutations of cities.
        
        Returns:
            set: Initial population of individuals (lists of city indices).
        """
        population = set()  # Use a set to avoid duplicate individuals
        for _ in range(self.population_size):
            individual = list(range(self.num_points))  # Create a permutation of city indices
            random.shuffle(individual)  # Shuffle the permutation randomly
            population.add(tuple(individual))  # Add the individual to the population
        return population
    
    def fitness(self, path):
        """
        Calculates the fitness of a path based on its total distance (negative value for maximization).
        
        Args:
            path (list): Path representing the order of cities.
        
        Returns:
            float: Fitness value of the path.
        """
        return -self.total_distance(path)
    
    def total_distance(self, path):
        """
        Calculates the total distance of a path by summing distances between consecutive cities.
        
        Args:
            path (list): Path representing the order of cities.
        
        Returns:
            float: Total distance of the path.
        """
        total = 0
        for i in range(self.num_points - 1):
            total += self.distances[path[i]][path[i+1]]
        total += self.distances[path[-1]][path[0]]  # Add the distance from the last city to the starting city
        return total
    
    def mutate(self, individual):
        """
        Applies mutation to an individual with a certain probability.
        
        Args:
            individual (list): An individual representing a path.
        
        Returns:
            list: Mutated individual.
        """
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(self.num_points), 2)  # Select two distinct indices
            individual[i], individual[j] = individual[j], individual[i]  # Swap the cities at those indices
        return individual
    
    def crossover(self, parent1, parent2):
        """
        Applies crossover to create a new child from two parent individuals.
        
        Args:
            parent1 (list): First parent individual.
            parent2 (list): Second parent individual.
        
        Returns:
            list: New child individual.
        """
        start = random.randint(0, self.num_points - 1)  # Choose a random start index
        end = random.randint(start + 1, self.num_points)  # Choose a random end index
        
        child = [-1] * self.num_points
        for i in range(start, end):
            child[i] = parent1[i]  # Copy the genes from parent1 to the child
        
        remaining = [gene for gene in parent2 if gene not in child]  # Get the remaining genes from parent2
        remaining_index = 0
        for i in range(self.num_points):
            if child[i] == -1:
                child[i] = remaining[remaining_index]  # Fill in the remaining genes in the child
                remaining_index += 1
        
        return child
    
    def evolve(self):
        """
        Evolves the population over a number of generations using the Genetic Algorithm.
        
        Returns:
            tuple: Best path found and its corresponding best distance.
        """
        for _ in range(self.generations):
            new_population = []  # Create a new population for the next generation
            sorted_population = sorted(self.population, key=self.fitness)  # Sort population by fitness
            elite_count = int(self.population_size * 0.2)  # Select the top 20% as elites
            new_population.extend(sorted_population[:elite_count])  # Add elites to the new population
            
            while len(new_population) < self.population_size:
                parent1 = random.choice(sorted_population)  # Randomly choose parent1
                parent2 = random.choice(sorted_population)  # Randomly choose parent2
                child = self.crossover(parent1, parent2)  # Create a child using crossover
                child = self.mutate(child)  # Apply mutation to the child
                new_population.append(child)  # Add the child to the new population
            
            self.population = new_population  # Replace the old population with the new one
        
        best_path = max(self.population, key=self.fitness)  # Find the best path (max fitness)
        best_distance = -self.fitness(best_path)  # Calculate the actual best distance
        return best_path, best_distance  # Return the best path and its distance
    
def main():
    # Take input for the number of cities, coordinates, and distances
    Euclidean = sys.stdin.readline()
    num_points = int(sys.stdin.readline())
    # distances = [[0.0, 4.597411, 9.110738, 3.187861, 4.302992],
    #             [4.597411, 0.0, 13.285327, 5.736168, 4.420019],
    #             [9.110738, 13.285327, 0.0, 7.822640, 10.096052],
    #             [3.187861, 5.736168, 7.822640, 0.0, 2.419287],
    #             [4.302992, 4.420019, 10.096052, 2.419287, 0.0]]
    # coordinates = [(10.391379, 8.405525), 
    #                 (14.780237, 7.036543),
    #                 (1.511838, 6.366090),
    #                 (9.276912, 5.418818),
    #                 (11.376465, 4.216809)]
    coordinates = []
    for i in range(num_points):
        x, y = map(float, sys.stdin.readline().split())
        coordinates.append((x, y))
    
    distances = []
    for i in range(num_points):
        row = list(map(float, sys.stdin.readline().split()))
        distances.append(row)
    pathntour = []
    genetic_algorithm = GeneticAlgorithmTSP(coordinates, distances, num_points)  # Initialize the GA
    path = genetic_algorithm.evolve()[0]
    
    printpath(path)
    for _ in range(10):
        pathntour.append(genetic_algorithm.evolve())

    sorted_list = sorted(pathntour, key=lambda x: x[1])
    printpath(sorted_list[0][0])

def printpath(path):
    for p in path:
        sys.stdout.write(str(p))
        sys.stdout.write(" ")        
        # print(p, end=' ')
    sys.stdout.writelines("\n")
    # print()
if __name__ == "__main__":
    main()
