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
        self.len_g = 48

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

class IndividualMocker(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def get_y(self):
        return self.y

    def __lt__(self, other):
        return self.y < other.y

    def __str__(self):
        return "x: {0}, y: {1}".format(self.x, self.y)