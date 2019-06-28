import math

# Function that returns true if 'a' is any power of 'b'
def is_power(a, b):
    # 1 is the only power of itself
    if (b == 1):
        return (a == 1)
    # Example: 5^1 = 5 or 5^0 = 1
    if ((a == b) or (a == 1)):
        return True
    # -Infinity or 0^x = 0
    elif (a == 0 or b == 0):
        return False

    # Using method recursively
    return ((a % b) == 0 and is_power((a / b), b))


def is_power1(a, b):
    # 1 is the only power of itself
    if (b == 1):
        return (a == 1)
    # Example: 5^1 = 5 or 5^0 = 1
    if ((a == b) or (a == 1)):
        return True
    # -Infinity or 0^x = 0
    elif (a == 0 or b == 0):
        return False

    # Using variable iteration
    while (a % b == 0):
        a /= b
    
    return (a == 1)


def is_power2(a, b):
    # 1 is the only power of itself
    if (b == 1):
        return (a == 1)
    # Example: 5^1 = 5 or 5^0 = 1
    if ((a == b) or (a == 1)):
        return True
    # -Infinity or 0^x = 0
    elif (a == 0 or b == 0):
        return False

    # Recursively compute the power of b
    pow = 1
    while (pow < a):
        pow *= b

    # Check if the computer power and value given match
    return (pow == a)




print("Function is_power(a, b) using recursion.")
print(is_power(5, 5))       # True
print(is_power(25, 5))      # True
print(is_power(125, 25))    # False
print(is_power(1, 13))      # True
print(is_power(64, 4))      # True
print(is_power(27, 4))      # False
print(is_power(256, 2))     # True
print(is_power(25, 25))     # True
print(is_power(0, 34))      # False
print(is_power(10, 0))      # False
print(is_power(13, 1))      # False
print()

print("Func is_power1(a, b) using while loop")
print(is_power1(5, 5))       # True
print(is_power1(25, 5))      # True
print(is_power1(125, 25))    # False
print(is_power1(1, 13))      # True
print(is_power1(64, 4))      # True
print(is_power1(27, 4))      # False
print(is_power1(256, 2))     # True
print(is_power1(25, 25))     # True
print(is_power1(0, 34))      # False
print(is_power1(10, 0))      # False
print(is_power1(13, 1))      # False
print()

print("Func is_power2(a, b) using while loop to increment b power")
print(is_power2(5, 5))       # True
print(is_power2(25, 5))      # True
print(is_power2(125, 25))    # False
print(is_power2(1, 13))      # True
print(is_power2(64, 4))      # True
print(is_power2(27, 4))      # False
print(is_power2(256, 2))     # True
print(is_power2(25, 25))     # True
print(is_power2(0, 34))      # False
print(is_power2(10, 0))      # False
print(is_power2(13, 1))      # False
print()

