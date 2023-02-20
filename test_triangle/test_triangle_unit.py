import unittest
import math
from triangle import Triangle


class TestTriangleUnit(unittest.TestCase):

    def setUp(self):
        self.first = Triangle(9, 8, 7)

    def tearDown(self):
        del self.first

    def test_triangle_eq(self):
        print('test started')
        second = Triangle(7, 9, 8)
        self.assertEqual(self.first, second)

    def test_triangle_perimetr(self):
        self.assertEqual(self.first.perimetr(), 24)

    def test_triangle_with_same_corners(self):
        second = Triangle(14, 16, 18)
        self.assertTrue(self.first.with_same_corners(second))

    def test_triangle_square(self):
        self.assertEqual(self.first.square(), math.sqrt(720))

    def test_triangle_ne(self):
        second = Triangle(3, 5, 7)
        self.assertFalse(self.first == second)

    def test_triangle_lt(self):
        second = Triangle(10, 11, 12)
        self.assertLess(self.first.perimetr(), second.perimetr())

    def test_triangle_gt(self):
        second = Triangle(3, 4, 5)
        self.assertGreater(self.first.perimetr(), second.perimetr())

    def test_triangle_le(self):
        second = Triangle(10, 9, 9)
        third = Triangle(8, 9, 7)
        self.assertLessEqual(self.first.perimetr(), second.perimetr())
        self.assertLessEqual(self.first.perimetr(), third.perimetr())

    def test_triangle_ge(self):
        second = Triangle(3, 3, 5)
        third = Triangle(7, 9, 8)
        self.assertGreaterEqual(self.first.perimetr(), second.perimetr())
        self.assertGreaterEqual(self.first.perimetr(), third.perimetr())

    def test_triangle_is_right_angled(self):
        self.assertEqual(self.first.is_right_angled(), False)

    def test_triangle_is_right_triangle(self):
        self.assertEqual(self.first.is_right_triangle(), False)

    def test_triangle_two_sides_eq(self):
        self.assertEqual(self.first.two_sides_eq(), False)


if __name__ == '__main__':
    unittest.main()
