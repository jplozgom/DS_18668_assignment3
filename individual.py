import random
import math
import string


class Individual:
    """
        Individual in the population
    """

    def __init__(self, size):
        self.fitness = 0
        if size > 0:
            self.genes = self.generate_random_genes(size)
        else:
            self.genes = []

    # Fitness function: returns a floating points of "correct" characters
    def calc_fitness(self, target):
        score = 0

        # insert your code to calculate the individual fitness here
        for i in range(0, len(target)):
            if(target[i] == self.genes[i]):
                score += 1

        self.fitness = score / len(target)

    def __repr__(self):
        return ''.join(self.genes) + " -> fitness: " + str(self.fitness)

    @staticmethod
    def generate_random_genes(size):
        genes = []

        for i in range(size):
            genes.append(random.choice(string.ascii_letters))

        return genes

    # The crossover function selects pairs of individuals to be mated, generating a third individual (child)
    def crossover(self, partner, *args, **kwargs):
        # Crossover suggestion: child with half genes from one parent and half from the other parent
        if 'twoPointCrossOver' in kwargs and kwargs['twoPointCrossOver']:
            return self.twoPointCrossover(partner, kwargs)
        else:
            return self.onePointCrossover(partner, kwargs)

    # The crossover function selects pairs of individuals to be mated, generating a third individual (child)
    def onePointCrossover(self, partner, *args, **kwargs):
        # Crossover suggestion: child with half genes from one parent and half from the other parent
        ind_len = len(self.genes)
        crossOverPoint = random.randint(0, ind_len - 1)
        child1 = Individual(0)
        child2 = Individual(0)

        # apply crossOverPoint in one point
        for i in range(len(self.genes)):
            if i < crossOverPoint:
                child1.genes.append(self.genes[i])
                child2.genes.append(partner.genes[i])
            else:
                child1.genes.append(partner.genes[i])
                child2.genes.append(self.genes[i])
        return child1, child2


    # The crossover function selects pairs of individuals to be mated, generating a third individual (child)
    def twoPointCrossover(self, partner, *args, **kwargs):
        # Crossover suggestion: child with half genes from one parent and half from the other parent
        ind_len = len(self.genes)
        crossOverPoint = random.randint(0, math.ceil(ind_len / 2) - 2)
        crossOverPoint2 = random.randint(math.ceil(ind_len / 2), ind_len - 2)
        child1 = Individual(0)
        child2 = Individual(0)

        # apply crossOverPoint in one point
        for i in range(len(self.genes)):
            if i < crossOverPoint or i >= crossOverPoint2:
                child1.genes.append(self.genes[i])
                child2.genes.append(partner.genes[i])
            else:
                child1.genes.append(partner.genes[i])
                child2.genes.append(self.genes[i])
        return child1, child2

    # Mutation: based on a mutation probability, the function picks a new random character and replace a gene with it
    def mutate(self, mutation_rate, *args, **kwargs):

        """Mutates if p is less that mutation rate ... in other words it mutates with a probability equivalent to mutation rate """

        p = random.uniform(0, 1)
        if p <= mutation_rate:
            # code to mutate the individual here
            newGene = random.choice(string.ascii_letters)
            geneIndex = random.randint(0, len(self.genes) - 1)
            self.genes[geneIndex] = newGene
            # print("GENE MUTATED = " + str(geneIndex))




