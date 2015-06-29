from unittest import TestCase
from src.main.individual import GeneticIndividual
from src.test.helpers import GeneticFitnessMocker


class TestGeneticIndividual(TestCase):

    def setUp(self):
        self.f = GeneticFitnessMocker()

    def test_recombine(self):
        a = GeneticIndividual(0b010000100101110010110110101111111001001000000101, self.f)
        b = GeneticIndividual(0b001101111111100011010011101100110001010101000000, self.f)

        c1 = a.recombine(b, 10)
        self.assertEquals(c1.x, 0b010000100101110010110110101111111001000101000000)
        c2 = a.recombine(b, 1)
        self.assertEquals(c2.x, 0b010000100101110010110110101111111001001000000100)
        c3 = a.recombine(b, 47)
        self.assertEquals(c3.x, 0b001101111111100011010011101100110001010101000000)
        c4 = a.recombine(b, 27)
        self.assertEquals(c4.x, 0b010000100101110010110011101100110001010101000000)
