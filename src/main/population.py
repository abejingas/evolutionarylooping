from random import shuffle, choice, sample, uniform
from copy import deepcopy

from src.main.generation import Generation
from src.main.individual import Individual


class Population(object):

    def __init__(self, start_population, fitness_object, min_d, max_d):
        self.generations = []
        self.generation = self._generate(start_population,
                                         fitness_object,
                                         min_d,
                                         max_d)
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
        children.mutation(mutation_percentage)
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

    def _generate(self, start_population, fitness_object, min_d, max_d):
        # TODO update individual generation
        # so that generated individuals satisfy the following conditions:
        # - individual length is in the min_d and max_d boundaries.
        # - individual's time codes are in the time codes of the whole clip.
        generation = Generation()
        for _ in range(start_population):
            t1 = uniform(0, fitness_object.clip.duration)
            t2 = t1 + uniform(min_d, max_d) * choice([-1, 1])

            while not 0 <= t2 <= fitness_object.clip.duration:
                t2 = t1 + uniform(min_d, max_d) * choice([-1, 1])

            generation.individuals.append(
                Individual(sorted([t1, t2]), fitness_object)
            )
        return generation
