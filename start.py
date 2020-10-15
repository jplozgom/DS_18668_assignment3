from population import Population


def main():
    pop_size = 2000
    target = "To be or not to be."
    mutation_rate = 0.05
    cross_over_points = 2
    generations_limit = 5000

    pop = Population(target, pop_size, mutation_rate, cross_over_points)
    # testing(pop)

    # """
    # Uncomment these lines bellow when you implement all the functions
    # """

    while not pop.finished:
        pop.generate_new_population()
        pop.evaluate()
        pop.print_population_status()

        if pop.generations > generations_limit:
            break

    print("hey")


def testing(pop):
    # you don't need to call this function when the ones right bellow are fully implemented
    pop.print_population_status()
    pop.natural_selection()
    pop.generate_new_population()
    pop.evaluate()
    pop.print_population_status()

if __name__ == "__main__":
    main()
