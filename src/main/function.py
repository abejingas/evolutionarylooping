import logging
from random import randint
import numpy as np


class FrameDistance(object):

    def __init__(self, clip, min_d=None, max_d=None):
        self.clip = clip
        self.N_pixels = clip.w * clip.h * 3
        self.min_d = min_d if min_d else 1
        self.max_d = max_d if max_d else 10

    def _dot_product(self, f1, f2):
        return (f1*f2).sum()/self.N_pixels

    def _distance(self, t1, t2):
        f1 = self.clip.get_frame(t1)
        f2 = self.clip.get_frame(t2)
        uv = self._dot_product(f1, f2)
        flat_f1 = 1.0*f1.flatten()
        flat_f2 = 1.0*f2.flatten()
        u = self._dot_product(flat_f1, flat_f1)
        v = self._dot_product(flat_f2, flat_f2)
        return np.sqrt(u+v - 2*uv)

    def fitness(self, x):
        if not self.min_d <= x[1] - x[0] <= self.max_d:
            # individual's duration not in wanted interval
            logging.warning("Individual out of duration bounds: {0}".format(x))
            return float("inf")
        if x[1] > self.clip.duration or x[0] < 0:
            # individual's time limits out of video's boundaries
            logging.warning("Individual out of video's bounds: {0}".format(x))
            return float("inf")
        return self._distance(x[0], x[1])


class GeneticFrameDistance(FrameDistance):

    def __init__(self, clip, min_d=None, max_d=None):
        super().__init__(clip, min_d, max_d)
        self.fps = self.clip.fps
        self.min_f = int(self.min_d * self.fps)
        self.max_f = int(self.max_d * self.fps)
        self.frames = int(self.clip.duration * self.fps)
        self.len_g = 48
        self.len_x = 32
        self.len_y = 16

    def gene_to_frames(self, gene):
        if gene.__class__.__name__ == 'list':
            logging.info("debug!")
        n1 = gene >> (self.len_g - self.len_x)
        n2 = gene & (2**self.len_y - 1)
        f1 = n1 % self.frames
        f2 = f1 + self.min_f + (n2 % (self.max_f-self.min_f))
        t1 = f1 / self.fps
        t2 = f2 / self.fps
        return [t1, t2]

    def fitness(self, x):
        x = self.gene_to_frames(x)
        return super().fitness(x)

    @staticmethod
    def generate_gene():
        return randint(0, 2**48-1)
