from unittest import TestCase
from src.main.individual import Individual
from src.test.helpers import FitnessMocker


class TestIndividual(TestCase):

    def setUp(self):
        self.f = FitnessMocker()
        self.f.clip.duration = 100

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
        m = Individual([0, 5], self.f)
        for i in range(1000):
            m.mutate(20)
            self.assertTrue(self.f.min_d <= m.x[1] - m.x[0] <= self.f.max_d)
            self.assertTrue(0 <= m.x[0] < self.f.clip.duration - self.f.min_d)
            self.assertTrue(self.f.min_d < m.x[1] <= self.f.clip.duration)

    def test_get_y(self):
        i = Individual([2, 8], self.f)
        self.assertIsNone(i.y)
        self.assertEqual(i.get_y(), 10)
        i.x = [5, 9]
        i.x_changed = True
        self.assertEqual(i.y, 10)
        i.get_y()
        self.assertEqual(i.y, 14)
