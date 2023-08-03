# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.

import unittest


class Rectangle:
    def __init__(self, length, width=None):
        if not width:
            self.width = length
        else:
            self.width = width
        self.length = length

    def get_perimetr(self):
        return 2 * self.length + 2 * self.width

    def get_area(self):
        return self.length * self.width

    def __add__(self, other):
        width = self.width
        perimetr = self.get_perimetr() + other.get_perimetr()
        length = (perimetr - 2 * width) / 2
        return Rectangle(width, length)

    def __sub__(self, other):
        # width = min(self.width, self.length, other.width, other.length)
        perimetr = abs(self.get_perimetr() - other.get_perimetr())
        length = int(perimetr / 4)
        width = perimetr / 2
        return Rectangle(length, width)

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Rectangle(2, 2)
        self.r2 = Rectangle(3, 3)
        self.r3 = Rectangle(1, 1)

    def test_add_perimetr(self):
        self.assertEqual(self.r1 + self.r2, Rectangle(2, 8))

    def test_create(self):
        self.assertEqual(Rectangle(2, 2), self.r1)

    def test_eq_perimetr(self):
        self.assertEqual(Rectangle(2, 2).get_perimetr(), 8)

    def test_area(self):
        self.assertEqual(self.r1.get_area(), 4)


unittest.main(verbosity=2)