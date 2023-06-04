import sys
from Functions import add, sub, mul, div, power

operator = (sys.argv[2])
n1 = int(sys.argv[1])
n2 = int(sys.argv[3])

if operator == '+':
  r = add(n1, n2)

if operator == '-':
  r = sub(n1, n2)

if operator == 'x':
  r = mul(n1, n2)

if operator == '/':
  r = div(n1, n2)

if operator == 'pw':
  r = power(n1, n2)

  
print(r)
