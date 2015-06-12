from random import random, randint, shuffle, uniform, choice
import logging

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

    # TODO make sure that the muatation doesn't screw up the duration time of the interval.
    def mutate(self, max_difference):
    #     # help vars
    #     duration = self.fitness_object.clip.duration
    #     min_d = self.fitness_object.min_d
    #     max_d = self.fitness_object.max_d
    #     o = [0, 1]
    #     shuffle(o)     # decide in which order the elements are touched
    #
    #     # mutate first element
    #     self.x[o[0]] = Individual._push_into_border(self.x[o[0]], max_difference, duration)
    #     self.x[o[0]] += uniform(-max_difference, max_difference)
    #
    #     # if the duration of the individual is out of range, mutate second element
    #     if not min_d <= abs(self.x[o[1]] - self.x[o[0]]) <= max_d:
    #         start = self.x[o[0]]
    #         start -= Individual._push_into_border(self.x[o[0]], max_difference, duration)
    #         self.x[o[1]] = start + uniform(min_d, max_d) * choice([-1, 1])
    #     self.x.sort()
    #     self.x_changed = True
    #
    # def mutate_new(self, max_difference):
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