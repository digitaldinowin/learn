import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
  calculator = Calculator()

  def testChecker1(self):
    self.assertFalse(Calculator.checker1(1, 1, 2))
    self.assertTrue(Calculator.checker1(1, 0, 2))

  def testChecker2(self):
    self.assertTrue(Calculator.checker2(1, 1, 2))
    self.assertFalse(Calculator.checker2(1, 0, 2))

  def testCalculate(self):
    return False

if __name__ == '__main__':
  unittest.main()