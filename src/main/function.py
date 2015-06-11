import numpy as np

class FrameDistance(object):

    def __init__(self, clip, min_d = None, max_d = None):
        self.clip = clip
        self.N_pixels = clip.w * clip.h * 3
        self.min_d = min_d if min_d else 1
        self.max_d = max_d if max_d else 10

    def _dot_product(self, F1, F2):
        return (F1*F2).sum()/self.N_pixels

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
            # individual's duration out of wanted interaval
            return float("inf")
        if x[1] > self.clip.duration or x[0] < 0:
            # individual's time limits out of video's boundaries
            return float("inf")
        return self._distance(x[0], x[1])
