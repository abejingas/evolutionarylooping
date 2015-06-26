from random import shuffle, choice, uniform
from src.main.generation import Generation, GeneticGeneration
from src.main.individual import Individual, GeneticIndividual


class Population(object):

    def __init__(self, start_population, fitness_object, min_d, max_d):
        self.generations = []
        self.generation = Population._generate(start_population,
                                               fitness_object,
                                               min_d,
                                               max_d)
        self.max_d = max_d
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
        # Remove elites from parent generation
        elites = [self.generation.individuals.pop(0) for _ in range(elites)]
        # Recombine the parents to new children
        children = self.generation.recombination(recombination_percentage)
        # Recombine the elites especially
        children.individuals.extend([
            elite.recombine(choice(self.generation.individuals))
            for _ in range(elite_recombinations)
            for elite in elites
        ])
        # Put parents and children all into one generation (without elites)
        children.individuals.extend(self.generation.individuals)
        # Select the lucky ones - EVALUATION!
        children = children.selection(selector)
        # Mutate some of them
        children.mutation(mutation_percentage, self.max_d*2)
        # Put the elites back into the child generation
        children.individuals.extend(elites)

        self.generation = children
        self.generation.individuals.sort()
        # self.generations.append(deepcopy(self.generation))

    def next_final_generation(self, recombination_percentage, selector):
        children = self.generation.recombination(recombination_percentage)
        children.individuals.extend(self.generation.individuals)
        children = children.selection(selector)
        self.generation = children
        # self.generations.append(deepcopy(self.generation))

    def __str__(self):
        population = ""
        for p in self.generations:
            population += str(p) + "\n\n"
        return population

    @staticmethod
    def _generate(start_population, fitness_object, min_d, max_d):
        generation = Generation()
        for i in range(start_population):
            t1 = uniform(0, fitness_object.clip.duration)
            t2 = t1 + uniform(min_d, max_d) * choice([-1, 1])

            while not 0 <= t2 <= fitness_object.clip.duration:
                t2 = t1 + uniform(min_d, max_d) * choice([-1, 1])

            generation.individuals.append(
                Individual(sorted([t1, t2]), fitness_object)
            )
        return generation


class GeneticPopulation(object):

    def __init__(self, popsize, f):
        self.generation = GeneticPopulation._generate(popsize, f)

    def next_generation(self, mutation_rate, selector, elites=0):
        elites = [self.generation.individuals.pop(0) for _ in range(elites)]
        mates = selector.select(self.generation)
        children = self.generation.recombination(mates)
        children.mutation(mutation_rate)
        children.individuals.extend(elites)
        self.generation = children
        self.generation.individuals.sort()

    @staticmethod
    def _generate(popsize, f):
        generation = GeneticGeneration()
        for i in range(popsize):
            generation.individuals.append(GeneticIndividual(f.generate_gene(), f))
        return generation
