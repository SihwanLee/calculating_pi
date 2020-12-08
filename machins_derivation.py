# Machin's Derivation

import math, decimal

decimal.getcontext().prec = 50

n = 1

while True:
	x = decimal.Decimal(1/5)
	y = decimal.Decimal(1/239)
	arctan_5 = x
	arctan_239 = y
	if n%2 == 1:
		arctan_5 = arctan_5 - decimal.Decimal(decimal.Decimal(x**(2*n+1)) / (2*n+1))
		arctan_239 = arctan_239 - decimal.Decimal(decimal.Decimal(x**(2*n+1)) / (2*n+1))
	elif n%2 == 0:
		arctan_5 = arctan_5 + decimal.Decimal(decimal.Decimal(x**(2*n+1)) / (2*n+1))
		arctan_239 = arctan_239 + decimal.Decimal(decimal.Decimal(x**(2*n+1)) / (2*n+1))
	n += 1
	print(decimal.Decimal(4*decimal.Decimal(4*arctan_5 - arctan_239)))