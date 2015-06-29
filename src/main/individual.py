from random import random, randint, shuffle, uniform, choice
import logging
import numpy as np


class Individual(object):

    def __init__(self, x, fitness_object):
        self.x = x
        self.fitness_object = fitness_object
        self.x_changed = True
        self.y = None

    def recombine(self, partner, weight=None):
        """
        Recombine the individual with another individual, the partner to create a child.
        The lower the weight, the lower the influence of the partner on the child.
        The higher the weight, the higher the influence of the partner on the child.
        :param partner: The partner (Individual object)
        :param weight: The weight (Integer between 0 and 1)
        :return: The child individual.
        """
        if not weight:
            weight = np.random.normal(0.5, 0.5)
        elif not 0 <= weight <= 1:
            raise ValueError("Weight must be between 0 and 1")
        return Individual(
            [(1 - weight) * self.x[i] + weight * partner.x[i] for i in range(len(self.x))],
            self.fitness_object
        )

    def mutate(self, max_difference):
        duration = self.fitness_object.clip.duration
        min_d = self.fitness_object.min_d
        max_d = self.fitness_object.max_d
        o = [0, 1]
        shuffle(o)

        # move t2 around t1
        self.x[o[1]] = self.x[o[0]] + uniform(min_d, max_d) * choice([-1, 1])
        self.x.sort()
        d_x = self.x[1] - self.x[0]

        # move both timestamps inside the border
        if self.x[1] + max_difference > duration:
            self.x[1] = duration - max_difference
            self.x[0] = duration - max_difference - d_x
        elif self.x[0] - max_difference < 0:
            self.x[0] = max_difference
            self.x[1] = max_difference + d_x
        d_i = uniform(-max_difference, max_difference)
        self.x = [i + d_i for i in self.x]

    @staticmethod
    def _push_into_border(t, max_change, clip_duration):
        """
        Modify the given time t so that it has a distance of max_change from the interval [0, clip_duration]
        :param t: the given time
        'param max_change: the maximum change of the time t
        :param clip_duration: the duration of the clip
        :return: the new time
        """
        if t + max_change > clip_duration:
            return clip_duration - max_change
        if t - max_change < clip_duration:
            return max_change
        return t

    def get_y(self):
        if self.x_changed:
            logging.debug("Evaluating individual...")
            self.y = self.fitness_object.fitness(self.x)
            self.x_changed = False
        return self.y

    def __lt__(self, other):
        return self.get_y() < other.get_y()

    def __str__(self):
        return 'x: [' + (', '.join(map(str, self.x))) + '], y: ' + str(self.get_y())


class GeneticIndividual(Individual):
    def recombine(self, partner, k=None):
        """
        Exercise a crossover between this individual and the partner.
        Example:
        Parents:    0 1 1 0 1 (self)
                    1 0 1 1 0 (partner)
        Cross-Site:      |
        Child:      0 1 1 1 0
        :param partner: The partner
        :param k:       The Cross-Site (index right to left)
        :return:        The new individual
        """
        l = self.fitness_object.len_g
        k = randint(1, l - 1) if k is None or not (1 <= k <= l - 1) else k

        c1 = (self.x >> k)
        c2 = partner.x & 2**k - 1
        c = (c1 << k) | c2
        return GeneticIndividual(c, self.fitness_object)

    def mutate(self, mutation_rate=0.001):
        for i in range(self.fitness_object.len_g):
            if random() < mutation_rate:
                self.x ^= (1 << i)

    def __str__(self):
        return "x: {0}, y: {1}".format(bin(self.x), self.get_y())
