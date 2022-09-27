import unittest
from Calculator import Calculator # из файла Калькулятор импортируем класс Калькулятор

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(4, 2)

    def test_add(self):
        self.assertEquals(self.calculator.add(), 6)

    def test_mult(self):
        self.assertEquals(self.calculator.mult(), 8)

    def test_subtr(self):
        self.assertEquals(self.calculator.subtr(), 2)

    def test_div(self):
        self.assertEquals(self.calculator.div(), 2)

if __name__ == "__main__":
    unittest.main