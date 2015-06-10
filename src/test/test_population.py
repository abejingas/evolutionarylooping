from unittest import TestCase

from src.main.population import Population
from src.test.helpers import FitnessMocker


class TestPopulation(TestCase):
    def setUp(self):
        self.f = FitnessMocker()

    def test__generate(self):
        p = Population(20, self.f, 1.5, 3.5)
        print(p.generation)
