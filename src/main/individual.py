from random import random, randint


class Individual(object):

    def __init__(self, x, fitness_object):
        self.x = x
        self.fitness_object = fitness_object
        self.x_changed = True
        self.y = None

    def recombine(self, partner, weight = None):
        """
        Recombine the individual with another individual, the partner to create a child.
        The lower the weight, the lower the influence of the partner on the child.
        The higher the weight, the higher the influence of the partner on the child.
        :param partner: The partner (Individual object)
        :param weight: The weight (Integer between 0 and 1)
        :return: The child individual.
        """
        if not weight:
            weight = 0.5 * random() + 0.25
        elif not 0 <= weight <= 1:
            raise ValueError("Weight must be between 0 and 1")
        return Individual(
            [(1-weight) * self.x[i] + weight * partner.x[i] for i in range(len(self.x))],
            self.fitness_object
        )

    def mutate(self, max_difference):
        for i in range(len(self.x)):
            if self.x[i] + max_difference > self.fitness_object.clip.duration:
                self.x[i] = self.fitness_object.clip.duration - max_difference
            elif self.x[i] - max_difference < 0:
                self.x[i] = max_difference
            self.x[i] += self._random_mutation(max_difference)
        self.x.sort()
        self.x_changed = True

    def get_y(self):
        if self.x_changed:
            self.y = self.fitness_object.fitness(self.x)
        return self.y

    @staticmethod
    def _random_mutation(max_difference):
        return randint(-max_difference, max_difference)

    def __lt__(self, other):
        return self.get_y() < other.get_y()

    def __str__(self):
        return 'x: [' + (', '.join(map(str, self.x))) + '], y: ' + str(self.get_y())