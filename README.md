# Traveling Salesman Problem: A Comparative Study

**Author:** Areebah Suhail  

## Abstract
This report delves into a comprehensive study exploring various methodologies to solve the Traveling Salesman Problem (TSP). TSP, a significant combinatorial optimization challenge, holds vast applications in transportation, logistics, and networking. The study evaluates multiple strategies, ranging from simple search algorithms to advanced heuristic techniques, aiming to dissect and analyze their strengths and weaknesses in terms of solution quality, computational efficiency, and scalability.

## Index
1. **Abstract**
2. **Algorithms**
   - a. Simple Search Algorithm
   - b. Weighted A* (Wa*) Heuristic
   - c. Genetic Algorithm (GA) Approach
3. **Implementation Details**
4. **Performance Analysis**
   - a. Evaluation Criteria
5. **Observations**
   - a. Simple Search Algorithm
   - b. Weighted A* (Wa*) Heuristic
   - c. Genetic Algorithm (GA) Approach
6. **Conclusion and Future Work**

## Algorithms
### Simple Search Algorithm
This algorithm explores all possible permutations of cities to find the optimal tour. However, its factorial time complexity makes it infeasible for larger instances as the number of cities increases.

### Weighted A* (Wa*) Heuristic
Utilizing the Weighted A* heuristic aimed to enhance efficiency. Though effective in certain cases, it lacked consistency in finding optimal solutions across different instances, especially for more complex scenarios.

### Genetic Algorithm (GA) Approach
The GA consistently delivered competitive solutions across a range of problem instances. Notably, it scaled gracefully to larger instances without significant deterioration in performance, showcasing a balance between solution quality and computation time.

## Implementation Details
- **Input Handling:** Accepts user input, including city numbers, coordinates, and distances between cities, organized into appropriate data structures for processing.
- **Fitness Function:** Evaluates solution quality based on total tour distance, guiding the algorithm towards minimizing traveled distance.
- **Elitism and Selection:** Retains top-performing individuals across generations, contributing to a high-quality genetic pool.
- **Crossover and Mutation:** Generates new offspring by combining genetic material from parent chromosomes and introduces randomness through mutation to promote diversity.

## Performance Analysis
A rigorous evaluation based on solution quality and computation time was conducted across benchmark instances of varying sizes, sourced from publicly available datasets and synthetic data.

### Evaluation Criteria
1. **Solution Quality:** Solutions were compared against known optimal solutions or assessed based on proximity to the best-known solutions.
2. **Computation Time:** Measured the time required by each approach to arrive at a solution, crucial in understanding algorithmic efficiency.

## Observations
### Simple Search Algorithm
While effective for smaller instances, the algorithm's exponential time complexity hindered its practicality for real-world scenarios with a substantial number of cities.

### Weighted A* Heuristic
Demonstrated improvements in computation time but lacked consistency in finding optimal solutions across various instances, especially those requiring deeper exploration of the solution space.

### Genetic Algorithm (GA)
Consistently produced competitive solutions across a wide range of instances, showcasing scalability and a balance between solution quality and computation time.

## Conclusion and Future Work
Future prospects for this project are:
1. Optimization: Tune Genetic Algorithm parameters for better results on specific instances.
2. Heuristics: Innovate new heuristics beyond Weighted A* for improved guidance
3. Hybrids: Explore combining Genetic Algorithms with other methods for enhanced 
performance.
In conclusion, this study explored different strategies for solving the Traveling Salesman Problem. 
While the simple search algorithm and Weighted A* heuristic have their merits, the Genetic 
Algorithm proved to be a robust approach, offering a balance between solution quality and efficiency. 
Future work could involve fine-tuning GA parameters, experimenting with alternative heuristics, or 
exploring hybrid approaches to further enhance the solution process
