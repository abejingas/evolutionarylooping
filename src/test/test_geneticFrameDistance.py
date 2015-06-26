from unittest import TestCase
from src.main.function import GeneticFrameDistance
from src.test.helpers import FrameDistanceClipMocker
from bitstring import BitArray


class TestGeneticFrameDistance(TestCase):

    def test_gene_to_frames(self):
        fdm = FrameDistanceClipMocker()
        gfd = GeneticFrameDistance(fdm, 1, 10)

        self.assertEqual(gfd.min_f, 30)
        self.assertEqual(gfd.max_f, 300)

        frames = gfd.gene_to_frames(BitArray('bin=000111100011100100110101000011100100100110001101'))

        self.assertAlmostEqual(frames[0], 2187.1333, delta=1e-04)
        self.assertAlmostEqual(frames[1], 2195.7667, delta=1e-04)
