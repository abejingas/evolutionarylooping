from unittest import TestCase
from src.main.individual import Individual
from src.test.helpers import FitnessMocker


class TestIndividual(TestCase):

    def setUp(self):
        self.f = FitnessMocker()
        self.f.clip.duration = 20

    def test_recombine(self):
        p1 = Individual([0, 6], self.f)
        p2 = Individual([3, 9], self.f)
        result = p1.recombine(p2, 0.5)
        self.assertAlmostEqual(result.x[0], 1.5, delta=1e-10)
        self.assertAlmostEqual(result.x[1], 7.5, delta=1e-10)
        self.assertAlmostEqual(result.get_y(), 9, delta=1e-10)


    def test_recombine_weight(self):
        p1 = Individual([0, 5], self.f)
        p2 = Individual([3, 10], self.f)
        result = p1.recombine(p2, 0.1)
        self.assertAlmostEqual(result.x[0], 0.3, delta=1e-10)
        self.assertAlmostEqual(result.x[1], 5.5, delta=1e-10)
        self.assertAlmostEqual(result.get_y(), 5.8, delta=1e-10)

    def test_mutate(self):
        m = Individual([5, 8], self.f)
        m.mutate(6)
        self.assertTrue(0 <= m.x[0] <= 12)
        self.assertTrue(2 <= m.x[1] <= 14)
        self.assertTrue(m.x_changed)

    def test_mutate_upper_limits(self):
        class PositiveMutationTestIndividual(Individual):
            @staticmethod
            def _random_mutation(max_difference):
                return max_difference

        # All clear case.
        m = PositiveMutationTestIndividual([5, 13], self.f)
        m.mutate(3)
        self.assertEqual(m.x, [8, 16])

        # Upper limitation case.
        m = PositiveMutationTestIndividual([8, 16], self.f)
        m.mutate(4)
        self.assertEqual(m.x, [12, 20])

        # Upper limit case.
        m = PositiveMutationTestIndividual([8, 16], self.f)
        m.mutate(5)
        self.assertEqual(m.x, [13, 20])

        # Lower limit case.
        m = PositiveMutationTestIndividual([4, 10], self.f)
        m.mutate(5)
        self.assertEqual(m.x, [10, 15])

    def test_mutate_lower_limits(self):
        class NegativeMutationTestIndividual(Individual):
            @staticmethod
            def _random_mutation(max_difference):
                return -max_difference

        # All clear case.
        m = NegativeMutationTestIndividual([5, 10], self.f)
        m.mutate(3)
        self.assertEqual(m.x, [2, 7])

        # Lower Limitation case.
        m = NegativeMutationTestIndividual([5, 10], self.f)
        m.mutate(5)
        self.assertEqual(m.x, [0, 5])

        # Lower limit case.
        m = NegativeMutationTestIndividual([5, 10], self.f)
        m.mutate(8)
        self.assertEqual(m.x, [0, 2])

        # Upper limit case.
        m = NegativeMutationTestIndividual([5, 18], self.f)
        m.mutate(3)
        self.assertEqual(m.x, [2, 14])

    def test_get_y(self):
        i = Individual([2, 8], self.f)
        self.assertIsNone(i.y)
        self.assertEqual(i.get_y(), 10)
        i.x = [5, 9]
        self.assertEqual(i.y, 10)
        i.get_y()
        self.assertEqual(i.y, 14)
