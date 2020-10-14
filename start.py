from population import Population


def main():
    pop_size = 200
    target = "To be or not to be."
    mutation_rate = 0.2
    cross_over_points = 2

    pop = Population(target, pop_size, mutation_rate, cross_over_points)
    # testing(pop)

    # you don't need to call this function when the ones right bellow are fully implemented
    pop.print_population_status()
    # pop.natural_selection()
    # pop.generate_new_population()
    # pop.evaluate()
    # pop.print_population_status()
    # print(pop.mating_pool)
    """
    Uncomment these lines bellow when you implement all the functions
    """

    while not pop.finished:
        pop.generate_new_population()
        pop.evaluate()
        pop.print_population_status()

        if pop.generations > 1500:
            break

    # print("hey")


def testing(pop):
    for i in range(0, len(pop.population) - 1, 2):
        print("\n\n----------------\n")
        print("Parents :\n")
        ind1 = pop.population[i]
        ind2 = pop.population[i+1]
        print(ind1.genes)
        print(ind2.genes)

        child1, child2 = ind1.crossover(ind2, twoPointCrossOver = True)
        child1.mutate(0.01)
        child2.mutate(0.01)
        print("\nChilds :\n")
        print(child1.genes)
        print(child2.genes)

if __name__ == "__main__":
    main()
