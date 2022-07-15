import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
  calculator = Calculator()

  def testMethod1(self):
    self.assertFalse(self.calculator.method1(1, 1, 2))
    self.assertTrue(self.calculator.method1(1, 0, 2))

  def testMethod2(self):
    self.assertTrue(self.calculator.method2(1, 1, 2))
    self.assertFalse(self.calculator.method2(1, 0, 2))

if __name__ == '__main__':
  unittest.main()