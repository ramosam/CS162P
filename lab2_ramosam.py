"""
Consider the following:
 X^15 is X * (X^14)
 X^14 is (X^7) * (X^7)
 X^7 is X * (X^6)
 X^6 is (X^3) * (X^3)
 X^3 is X * (X^2)
 X^2 is X * X
 X is X
"""

# Recursive Lab
def special_base_to_power(base, expon):
    if expon <= 0:
        return 1
    sum = 0
    if expon % 2 == 0:
        sum += special_base_to_power(base, expon/2) * special_base_to_power(base, expon/2)
    else:
        sum += base * special_base_to_power(base, expon-1)
    return sum

print(special_base_to_power(5, 1))      # 5
print(special_base_to_power(2, 13))     # 8192
print(special_base_to_power(3, 6))      # 729
print(special_base_to_power(5, 8))      # 390625
print(special_base_to_power(27, 0))     # 1
print(special_base_to_power(13, -1))    # 1
