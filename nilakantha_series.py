# Nilakantha Series

import decimal, math


decimal.getcontext().prec =  250

pi = decimal.Decimal(3)
n = decimal.Decimal(1)
while True:
	if n%2 == 1:
		pi = decimal.Decimal(pi) + decimal.Decimal(4/((2*n)*(2*n+1)*(2*n+2)))
	elif n%2 == 0:
		pi = decimal.Decimal(pi) - decimal.Decimal(4/((2*n)*(2*n+1)*(2*n+2)))
	n += 1
	print(pi)