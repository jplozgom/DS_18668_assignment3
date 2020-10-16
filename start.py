from population import Population
import time


def main():
    pop_size = 2000
    target = "To be or not to be."
    mutation_rate = 0.02
    cross_over_points = 2
    generations_limit = 5000
    start_time = time.time()
    testingMode  = False
    pop = Population(target, pop_size, mutation_rate, cross_over_points)

    if(testingMode):
        testing(pop)
    else:
        while not pop.finished:
            pop.generate_new_population()
            pop.evaluate()
            pop.print_population_status()

            if pop.generations > generations_limit:
                break

        end_time = time.time()

        print("\n\n/******* SUMMARY *****/\n\n")
        print("Execution time = %s seconds " % (end_time - start_time))
        print("Population size = " + str(pop_size))
        print("Generations = " + str(pop.generations))
        print("Mutation rate = " + str(mutation_rate))
        print("Crossovers points = " + str(cross_over_points))
        print("Avg Fitness all generations = " + str(pop.generation_fitnesses_sum / pop.generations))
        print("Fitness last generations = " + str(pop.average_fitness))
        print("Finished = " + str(pop.finished))
        print("Best individual = " + "".join(pop.best_ind.genes))
        print("Best individual fitness = " + str(pop.best_ind.fitness))
        print("\n\n/******* END SUMMARY *****/\n\n")

def testing(pop):
    # you don't need to call this function when the ones right bellow are fully implemented
    pop.print_population_status()
    pop.natural_selection()
    pop.generate_new_population()
    pop.evaluate()
    pop.print_population_status()



if __name__ == "__main__":
    main()
