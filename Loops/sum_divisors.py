#!/usr/bin/env python3

def sum_divisors(n):
    return sum([i for i in range(1, n)
                if n % i == 0])

print(sum_divisors(0))
print(sum_divisors(3)) # Should sum of 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
