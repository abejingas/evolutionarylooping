from random import shuffle, choice, sample
from src.Generation import Generation
from copy import deepcopy
from src.Individual import Individual


class Population(object):

    def __init__(self, start_population, function, parameters):
        self.function = function
        self.generations = []
        self.generation = self._generate(start_population, parameters)

        self.generations.append(self.generation)

    @staticmethod
    def _shuffled_list(size):
        l = list(range(size))
        shuffle(l)
        return l

    def next_generation(self,
                        elites,
                        elite_recombinations,
                        recombination_percentage,
                        mutation_percentage,
                        mutation_type,
                        selector):
        self.generation.individuals.sort()

        elites = [self.generation.individuals.pop(0) for _ in range(elites)]
        children = self.generation.recombination(recombination_percentage)
        children.individuals.extend([
            elite.recombine(choice(self.generation.individuals))
            for _ in range(elite_recombinations)
            for elite in elites
        ])
        children.individuals.extend(self.generation.individuals)
        children = children.selection(selector)
        children.mutation(mutation_percentage, mutation_type)
        children.individuals.extend(elites)

        self.generation = children
        self.generation.individuals.sort()
        self.generations.append(deepcopy(self.generation))

    def next_final_generation(self, recombination_percentage, selector):
        children = self.generation.recombination(recombination_percentage)
        children = children.selection(selector)
        self.generation = children
        self.generations.append(deepcopy(self.generation))

    def __str__(self):
        population = ""
        for p in self.generations:
            population += str(p) + "\n\n"
        return population

    def _generate(self, start_population, parameters):
        generation = Generation()
        generation.individuals = [
            Individual(
                sample(range(parameters), parameters),
                self.function
            ) for _ in range(start_population)
        ]
        return generation
