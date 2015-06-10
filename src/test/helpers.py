__author__ = 'Leon'


class FitnessMocker(object):
    def __init__(self):
        self.clip = ClipMocker()

    def fitness(self, x):
        return sum(x)


class ClipMocker(object):
    def __init__(self):
        self.duration = 100