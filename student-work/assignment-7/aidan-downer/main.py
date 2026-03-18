#!/usr/bin/env python3
import math

print("All prime numbers from 1 to 100:")
for i in range(3, 101):
	prime = True
	max = int(math.sqrt(i)) + 1
	for j in range(2, max):
		if i % j == 0:
			prime = False
			break
	if prime:
		print(f"{i} is prime")

