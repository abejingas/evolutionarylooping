__author__ = 'Leon'


class FitnessMocker(object):
    def __init__(self):
        self.clip = ClipMocker()
        self.min_d = 1
        self.max_d = 10

    def fitness(self, x):
        return sum(x)


class ClipMocker(object):
    def __init__(self):
        self.duration = 100