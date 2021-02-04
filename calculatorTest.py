import unittest
import calculator

class TestCase(unittest.TestCase):
    def test_add(self):
        result = calculator.add(5, 12)
        self.assertEqual(result, 17)
    def test_subtract(self):
        result = calculator.subtract(12, 5)
        self.assertEqual(result, 7)
        result = calculator.subtract(5, 12)
        self.assertEqual(result, -7)
    def test_multiply(self):
        result = calculator.multiply(4, 6)
        self.assertEqual(result, 24)
    def test_divide(self):
        result = calculator.divide(10, 5)
        self.assertEqual(result, 2)
        result = calculator.divide(5, 0)
        self.assertEqual(result, None)
        result = calculator.divide(5, 10)
        self.assertEqual(result, 0.5)
if __name__ == '__main__':
    unittest.main(verbosity=2)

    