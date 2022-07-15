class Calculator:
  def checker1(a, b, c):
    return a + b < c

  def checker2(a, b, c):
    if b != 0:
      return a / b < c
    else:
      return False
  
  def calculate(self, m, n, s):
    t = 0
    if Calculator.checker1(m, n, s):
      t = 1.12
    elif Calculator.checker2(m, n, s):
      t = 2.07

    return t

if __name__ == '__main__':
  t = Calculator().calculate(1, 1, 2)
  print('%.1f' % t)