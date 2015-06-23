from unittest import TestCase
from src.main.function import GeneticFrameDistance
from src.test.helpers import FrameDistanceClipMocker
__author__ = 'Leon'

class TestGeneticFrameDistance(TestCase):

    def test_gene_to_frames(self):
        fdm = FrameDistanceClipMocker()
        gfd = GeneticFrameDistance(fdm, 1, 10)

        self.assertEqual(gfd.min_f, 30)
        self.assertEqual(gfd.max_f, 300)

        frames = gfd.

    def test_fitness(self):
        self.fail()
