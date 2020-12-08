# Chudnovsky Method

import math, decimal
decimal.getcontext().prec = 100

pi=0
before = 0

for n in range(0, 17):
	numerator = decimal.Decimal(((-1)**n)*(math.factorial(6*n))*(13591409+545140134*n))
	denominator = decimal.Decimal(math.factorial(3*n)*((math.factorial(n))**3)*(640320**((3*n)+(3/2))))
	before += decimal.Decimal(numerator/denominator)
pi = decimal.Decimal(1/(12*before))
print(pi)
