"""Write a program that take an integer and tests whether
the n-th bit in the binary representation of that integer is set or not.

i.e., binary representation of 6 is:
    110

The least significant bit is the bit on the far right 
of the binary representation and the most significant
bit is the bit on the far left. We order the bits as 

b2, b1, b0
1   1   0

For our function, if we check the 0th bit, we should obtain
"False" as the binary value at b0 is 0

Alternativevly, if we check the 1st bit, we should obtain
"True" as the binary value at b1 is 1.
"""

"""
Observation: (how the bit shift operator works)
    1 << 0 : 0 0 0 0 0 0 1
    1 << 1 : 0 0 0 0 0 1 0
    1 << 2 : 0 0 0 0 1 0 0 

WE can combine the shift operator along with the same idea
that we saw in the even_odd video
"""

"""
Example: Is the 2nd bit set
    6 :      1 1 0
    1 << 2   1 0 0 &
             - - - 
             1 0 0

Example: Is the 0th bit set
    6 :      1 1 0
    1 << 0   0 0 1 &
             - - - 
             0 0 0

Observation:
    If we AND the result of shifting over by the n with
    the number in question, we obtain 0 or anything else.

    0 : n-th bit is NOT set.
      : n-th bit IS set.
"""


def is_nth_bit_set(x, n):
    if x & (1 << n):
        return True
    return False


# 2nd bit set for binary 6
print(is_nth_bit_set(6, 2))

# 3rd bit set for binary 6
print(is_nth_bit_set(6, 3))

# 0th bit set for binary 6
print(is_nth_bit_set(6, 0))

# 0th bit set for binary 6
print(is_nth_bit_set(7, 0))
