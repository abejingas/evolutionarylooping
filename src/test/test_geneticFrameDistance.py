from unittest import TestCase
from src.main.function import GeneticFrameDistance
from src.test.helpers import FrameDistanceClipMocker


class TestGeneticFrameDistance(TestCase):

    def test_gene_to_frames(self):
        fdm = FrameDistanceClipMocker()
        gfd = GeneticFrameDistance(fdm, 1, 10)

        self.assertEqual(gfd.min_f, 30)
        self.assertEqual(gfd.max_f, 300)

        # frames =  3 000 000
        # min_f  =         30
        # max_f  =        300
        # fps    =         30
        #
        # n1 =    507 065 614
        # n2 =         18 829
        #
        # m1 = n1 mod (frames - max_f) = 116 314
        # m2 = n2 mod (max_f - min_f)  =     199
        #
        # f1 = m1         = 116 314
        # f2 = m2 + min_f =     229
        #
        # t1 = f1 / fps        = 3877.1333
        # t2 = (f1 + f2) / fps = 3884.7667
        frames = gfd.gene_to_frames(0b000111100011100100110101000011100100100110001101)
        self.assertAlmostEqual(frames[0], 3877.1333, delta=1e-04)
        self.assertAlmostEqual(frames[1], 3884.7667, delta=1e-04)
