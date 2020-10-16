from individual import Individual
import random
import math


class Population:
    """
        A class that describes a population of virtual individuals
    """

    def __init__(self, target, size, mutation_rate, cross_over_points, *args, **kwargs):
        self.population = []
        self.populationSize = 0
        self.originalPopulationSize = size
        self.generations = 0
        self.target = target
        self.mutation_rate = mutation_rate
        self.cross_over_points = cross_over_points
        self.best_ind = None
        self.finished = False
        self.perfect_score = 1.0
        self.max_fitness = 0.0
        self.pop_fitness_sum = 0.0 # sum of the population individuals fitneses
        self.average_fitness = 0.0 # average of the population fitness
        self.generation_fitnesses_sum = 0
        self.mating_pool = []
        self.generations_limit = None

        for i in range(size):
            ind = Individual(len(target))
            self.population.append(ind)

        self.calculateFitnessForEveryone()


    def calculateFitnessForEveryone(self):
        self.average_fitness = 0
        self.populationSize = len(self.population)
        self.max_fitness = 0
        for i in range(self.populationSize):
            self.population[i].calc_fitness(self.target)
            if self.population[i].fitness > self.max_fitness:
                self.max_fitness = self.population[i].fitness
                self.best_ind = self.population[i]

            self.average_fitness += self.population[i].fitness

        self.pop_fitness_sum = self.average_fitness
        self.average_fitness /= self.populationSize


    def print_population_status(self):
        print("\nPopulation #:" + str(self.generations))
        print("\nPopulation size: " + str(len(self.population)))
        print("Average fitness: " + str(self.average_fitness))
        print("Best individual: " + str(self.best_ind))

    # Generate a mating pool according to the probability of each individual
    def natural_selection(self):
        self.mating_pool = []
        fitnessSum = self.average_fitness * self.populationSize

        # # Implementation suggestion based on Lab 3:
        # # Based on fitness, each member will get added to the mating pool a certain number of times
        # # a higher fitness = more entries to mating pool = more likely to be picked as a parent
        # # a lower fitness = fewer entries to mating pool = less likely to be picked as a parent

        for i in range(self.originalPopulationSize):
            individual = self.population[i]
            appendTimes = int(round(( individual.fitness / fitnessSum ) * self.populationSize))

            # Searching for the position
            for j in range(appendTimes):
                self.mating_pool.append(i)
                if len(self.mating_pool) == len(self.population):
                    break

            if len(self.mating_pool) == len(self.population):
                break

    # Generate the new population based on the natural selection function
    def generate_new_population(self):

        newPopulation = []

        # 1. create mating pool
        self.natural_selection()


        # 2. for each pair of elements in the mating pool create two offsprings
        for i in range(0, self.populationSize, 2):
            # select two random values from the mating pool
            indexes = random.sample(range(0, len(self.mating_pool)), 2)
            parent1 = self.population[indexes[0]]
            parent2 = self.population[indexes[1]]

            # 3. mutate offspring if necessary
            child1, child2 = parent1.crossover(parent2, crossover_points=self.cross_over_points)
            child1.mutate(self.mutation_rate)
            child2.mutate(self.mutation_rate)

            #4. add to new population
            child1.calc_fitness(self.target)
            child2.calc_fitness(self.target)
            appended = 0

            if child1.fitness > parent1.fitness or child1.fitness > parent2.fitness:
                newPopulation.append(child1)
                appended += 1

            if child2.fitness > parent1.fitness or child2.fitness > parent2.fitness:
                newPopulation.append(child2)
                appended += 1

            if appended == 1:
                if parent1.fitness > parent2.fitness:
                    newPopulation.append(parent1)
                else:
                    newPopulation.append(parent2)
            elif appended == 0:
                newPopulation.append(parent1)
                newPopulation.append(parent2)

        # store the current population average fitness
        self.generation_fitnesses_sum += self.average_fitness
        self.population = newPopulation
        self.calculateFitnessForEveryone()

    # Compute/Identify the current "most fit" individual within the population
    def evaluate(self):
        self.generations += 1
        for ind in self.population:
            if self.best_ind == None or ind.fitness > self.max_fitness:
                self.max_fitness = ind.fitness
                self.best_ind = ind

            if self.best_ind.fitness == 1:
                self.finished = True
                break
