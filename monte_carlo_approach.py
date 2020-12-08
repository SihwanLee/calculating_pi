# Monte Carlo Approach

from random import uniform
import math, decimal, time

r = 2.0

circle_count = 0
total_count = 0

while True:
	x = decimal.Decimal(uniform(-r, r))
	y = decimal.Decimal(uniform(-r, r))

	distance = decimal.Decimal(math.sqrt((x**2)+(y**2)))

	if distance > 2:
		total_count += 1
	elif distance <= 2:
		total_count += 1
		circle_count += 1
	print(str(4*(decimal.Decimal(circle_count/total_count))))