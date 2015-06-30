from unittest import TestCase
from src.main.function import GeneticFrameDistance
from src.main.generation import GeneticGeneration
from src.main.selector import ParentSelector
from src.test.helpers import IndividualMocker


class TestParentSelector(TestCase):

    def test_select(self):
        g = GeneticGeneration()
        g.individuals = [
            IndividualMocker(0, 10),
            IndividualMocker(1, 1),
            IndividualMocker(2, 100),
            IndividualMocker(3, float("inf")),
            IndividualMocker(3, float("inf")),
            IndividualMocker(3, float("inf")),
            IndividualMocker(3, float("inf")),
            IndividualMocker(3, float("inf")),
            IndividualMocker(3, float("inf")),
            IndividualMocker(3, float("inf")),
            IndividualMocker(3, float("inf")),
            IndividualMocker(3, float("inf")),
            IndividualMocker(3, float("inf")),
            IndividualMocker(3, float("inf")),
            IndividualMocker(3, float("inf")),
            IndividualMocker(3, float("inf")),
            IndividualMocker(3, float("inf")),
            IndividualMocker(3, float("inf")),
            IndividualMocker(3, float("inf")),
            IndividualMocker(4, 9)
        ]
        s = ParentSelector(100)
        ng = s.select(g)
        print(ng)
        self.fail()
