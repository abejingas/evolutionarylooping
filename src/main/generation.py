from random import random, choice


class Generation(object):

    def __init__(self):
        self.individuals = []

    def recombination(self, recombination_percentage):
        next_gen = Generation()
        for individual in self.individuals:
            if random() < recombination_percentage:
                partner = self.retrieve_partner(individual)
                child = individual.recombine(partner)
                next_gen.individuals.append(child)
        return next_gen

    def mutation(self, mutation_percentage, max_difference):
        for individual in self.individuals:
            if random() < mutation_percentage:
                individual.mutate(max_difference)

    def selection(self, selector):
        return selector.select(self)

    def retrieve_partner(self, partner, mates=None):
        if mates is None:
            mates = self

        while True:
            individual = choice(mates.individuals)
            if partner is not individual:
                return individual

    def get_median_individual(self):
        return self.individuals[(len(self.individuals) - 1) // 2]

    def to_dict(self):
        return [{'x': i.x, 'y': i.y} for i in self.individuals]

    def __str__(self):
        return '\n'.join(str(i) for i in self.individuals)

class GeneticGeneration(Generation):

    def recombination(self, mates):
        next_gen = GeneticGeneration()
        for i in mates.individuals:
            next_gen.individuals.append(i.recombine(self.retrieve_partner(i)))
        return next_gen

    def mutation(self, mutation_rate):
        for i in self.individuals:
            i.mutate(mutation_rate)

    def retrieve_partner(self, partner, mates=None):
        if mates is None:
            mates = self

        while True:
            individual = choice(mates.individuals)
            if partner.x != individual.x:
                return individual

    def to_dict(self):
        return [{'x': bin(i.x), 'y': i.y} for i in self.individuals]
