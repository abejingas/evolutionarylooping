__author__ = 'Leon'


class FitnessMocker(object):
    def __init__(self):
        self.clip = ClipMocker()
        self.min_d = 1
        self.max_d = 10

    @staticmethod
    def fitness(self, x):
        return sum(x)


class GeneticFitnessMocker(object):
    def __init__(self):
        self.clip = ClipMocker()
        self.min_d = 1
        self.max_d = 10
        self.min_f = 30
        self.max_f = 300
        self.fps = 30
        self.frames = self.clip.duration * self.fps

    @staticmethod
    def fitness(x):
        return x.int


class ClipMocker(object):
    def __init__(self):
        self.duration = 100


class FrameDistanceClipMocker(object):
    def __init__(self):
        self.fps = 30
        self.duration = 100000
        self.w = 300
        self.h = 200
