from unittest import TestCase
from src.main.individual import Individual


class TestIndividual(TestCase):

    def setUp(self):
        self.f = lambda x: sum(x)

    def test_recombine(self):
        p1 = Individual([0, 6], self.f, 20)
        p2 = Individual([3, 9], self.f, 20)
        result = p1.recombine(p2, 0.5)
        self.assertEqual(result.x, [2, 8])
        self.assertEqual(result.y, 10)

    def test_recombine_weight(self):
        p1 = Individual([0, 5], self.f, 20)
        p2 = Individual([3, 10], self.f, 20)
        result = p1.recombine(p2, 0.1)
        self.assertEqual(result.x, [0, 6])
        self.assertEqual(result.y, 6)

    def test_mutate(self):
        m = Individual([5, 8], self.f, 20)
        m.mutate(6)
        self.assertTrue(0 <= m.x[0] <= 12)
        self.assertTrue(2 <= m.x[1] <= 14)
        self.assertEqual(sum(m.x), m.y)

    def test_mutate_upper_limits(self):
        class PositiveMutationTestIndividual(Individual):
            @staticmethod
            def _random_mutation(max_difference):
                return max_difference

        # All clear case.
        m = PositiveMutationTestIndividual([5, 13], self.f, 20)
        m.mutate(3)
        self.assertEqual(m.x, [8, 16])

        # Upper limitation case.
        m = PositiveMutationTestIndividual([8, 16], self.f, 20)
        m.mutate(4)
        self.assertEqual(m.x, [12, 20])

        # Upper limit case.
        m = PositiveMutationTestIndividual([8, 16], self.f, 20)
        m.mutate(5)
        self.assertEqual(m.x, [13, 20])

        # Lower limit case.
        m = PositiveMutationTestIndividual([4, 10], self.f, 20)
        m.mutate(5)
        self.assertEqual(m.x, [10, 15])

    def test_mutate_lower_limits(self):
        class NegativeMutationTestIndividual(Individual):
            @staticmethod
            def _random_mutation(max_difference):
                return -max_difference

        # All clear case.
        m = NegativeMutationTestIndividual([5, 10], self.f, 20)
        m.mutate(3)
        self.assertEqual(m.x, [2, 7])

        # Lower Limitation case.
        m = NegativeMutationTestIndividual([5, 10], self.f, 20)
        m.mutate(5)
        self.assertEqual(m.x, [0, 5])

        # Lower limit case.
        m = NegativeMutationTestIndividual([5, 10], self.f, 20)
        m.mutate(8)
        self.assertEqual(m.x, [0, 2])

        # Upper limit case.
        m = NegativeMutationTestIndividual([5, 18], self.f, 20)
        m.mutate(3)
        self.assertEqual(m.x, [2, 14])

    def test_function(self):
        i = Individual([2, 8], self.f, 10)
        self.assertEqual(i.y, 10)
