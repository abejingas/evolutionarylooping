from unittest import TestCase
from bitstring import BitArray
from src.main.individual import GeneticIndividual
from src.test.helpers import GeneticFitnessMocker


class TestGeneticIndividual(TestCase):

    def setUp(self):
        self.f = GeneticFitnessMocker()

    def test_recombine(self):
        a = GeneticIndividual(BitArray('bin=010000100101110010110110101111111001001000000101'), self.f)
        b = GeneticIndividual(BitArray('bin=001101111111100011010011101100110001010101000000'), self.f)
        c1 = a.recombine(b, 10)
        self.assertEqual(c1.x.bin, '010000100111100011010011101100110001010101000000')
        c2 = a.recombine(b, 1)
        self.assertEqual(c2.x.bin, '001101111111100011010011101100110001010101000000')
        c3 = a.recombine(b, 47)
        self.assertEqual(c3.x.bin, '010000100101110010110110101111111001001000000100')
        c4 = a.recombine(b, 27)
        self.assertEqual(c4.x.bin, '010000100101110010110110101100110001010101000000')
