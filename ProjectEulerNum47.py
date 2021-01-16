# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
from math import sqrt,ceil
import time
start = time.time()
answer = 0

def prime_factors(num):
    divisors = set()
    i = 2
    while i < ceil(sqrt(num)) or num == 1:
        if num % i == 0:
            num = int(num/i)
            divisors.add(i)
            i -=1
        i += 1
    return len(divisors) + 1

j = 2*3*5*7

while answer == 0:
    if prime_factors(j) == 4:
        j += 1
        if prime_factors(j) == 4:
            j += 1
            if prime_factors(j) == 4:
                j += 1
                if prime_factors(j) == 4:
                    answer += (j-3)
                    break
    j += 1

print(answer)

stop = time.time()
print("Time: ", stop-start)