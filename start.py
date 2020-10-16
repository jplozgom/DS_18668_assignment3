from population import Population
import time


def main():
    pop_size = 1000
    target = "To be or not to be."
    mutation_rate = 0.01
    testingMode  = False
    totalTrials = 20
    trials = {
        "sumAvgGenerations": 0,
        "sumPopFitnessAverage": 0,
        "sumExecutionTime": 0,
        "totalFinished": 0,
    }

    start_time = time.time()

    for i in range(totalTrials):
        results = executeGA(pop_size, mutation_rate, target, testingMode)
        if results is not None:
            trials['sumAvgGenerations'] += results['generations']
            trials['sumPopFitnessAverage'] += results['popFitnessAverage']
            trials['sumExecutionTime'] += results['executionTime']
            trials['totalFinished'] += results['finished']

    end_time = time.time()
    print("Total time AVG = %s seconds " % (end_time - start_time))
    print("Execution trial time AVG = %s seconds " % (trials['sumExecutionTime']/totalTrials))
    print("AVG of Generations =  "  + str(trials['sumAvgGenerations'] / totalTrials))
    print("Last population fitness AVG =  "  + str(trials['sumPopFitnessAverage'] / totalTrials))
    print("Trials completed =  "  + str(trials['totalFinished']))


def executeGA(populationSize, mutation_rate, target,testingMode):
    pop_size = populationSize
    target = "To be or not to be."
    mutation_rate = mutation_rate
    cross_over_points = 2
    generations_limit = 15000
    start_time = time.time()
    trialResults = {
        "generations": 0,
        "popFitnessAverage": 0
    }

    pop = Population(target, pop_size, mutation_rate, cross_over_points)

    if(testingMode):
        testing(pop)
        return None
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

        trialResults['generations'] = pop.generations
        trialResults['popFitnessAverage'] = pop.average_fitness
        trialResults['executionTime'] = end_time - start_time
        trialResults['finished'] = int(pop.finished)
        return trialResults

def testing(pop):
    # you don't need to call this function when the ones right bellow are fully implemented
    pop.print_population_status()
    pop.natural_selection()
    pop.generate_new_population()
    pop.evaluate()
    pop.print_population_status()



if __name__ == "__main__":
    main()
