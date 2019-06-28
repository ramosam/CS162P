""" Learning Outcomes
 By the end of this week, you should be able to:

 explain the difference between an iterative algorithm and a recursive algorithm

 list the three requirements for successful recursion
    - it has a base case that causes it to terminate
    - it calls itself
    - when it calls itself, the arguments move toward the base case
 convert a simple iterative function into its recursive equivalent
"""


def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if (n == 0):
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        print(space, 'returning', result)
        return result

# factorial(4)


def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

def print_n_iteration(s, n):
    # wanted to test while instead of if
    while n <= 0:
        return
    print(s)
    while n > 0:
        print_n_iteration(s, n-1)
        return
    


# print_n('sShort', 3)
# print_n_iteration('sIterated', 3)

# print_n('sShort', 6)
# print_n_iteration('sIterated', 6)

# print_n('sShort', 0)
# print_n_iteration('sIterated', 0)

# print("End")


### Simple Tail Recursion ###
# Iteration
def summer_of_numbers(value, sum):
    # termination case
    while value > 0:
        sum += value
        # decrement coutner
        value -= 1

    return sum

# print(summer_of_numbers(4, 0))

def summer_of_nums(value, sum):
    # base case terminates recursion
    # removed '=' so the sum includes adding 1
    if value < 1:
        return sum
    # computation
    sum += value
    # Recursion call
    return summer_of_nums(value-1, sum)

# print(summer_of_nums(4, 0))


