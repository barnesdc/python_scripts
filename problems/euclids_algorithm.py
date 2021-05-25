""" Euclid's Algorithm 
 Find the greatest common denominator (GCD) of two integers
 GCD = the largetst integer that divides both numbers without leaving a remainder
 e.g. GCD of 20 & 8 = 4

Steps:
1. For two integers a and b, where a > b, divide a by b.
2. If the remainder, r, is 0, then stop: GCD is B
3. Otherwise, set a to b, b to r, and repeat step 1 until r is 0

a | b | r
20| 8 | 4 -> repeat step 1
8 | 4 | 0 -> stop
"""


def gcd(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b

    return a


print(gcd(60, 96))
print(gcd(20, 8))
