class Calculator:
  def method1(self, a, b, c):
    return a + b < c

  def method2(self, a, b, c):
    if b != 0:
      return a / b < c
    else:
      return False