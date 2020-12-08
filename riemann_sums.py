# Riemann Sums

import math, decimal

decimal.getcontext().prec = 100

num_rectangle = decimal.Decimal(100000000)

delta_x = decimal.Decimal(1/num_rectangle)
x = decimal.Decimal(0)
pi = decimal.Decimal(0)

while x<1:
	f = decimal.Decimal(math.sqrt(decimal.Decimal(1-x**2)))
	pi += decimal.Decimal(f*delta_x)
	x += delta_x
pi = 4*pi
print(pi)
