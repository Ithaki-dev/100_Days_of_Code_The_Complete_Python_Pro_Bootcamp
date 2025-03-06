def add(*nums):
    """
    This function takes any number of integers as arguments and returns their sum.
    >>> add(1, 2, 3)
    6
    >>> add(4, 5, 6, 7, 8)
    30
    """
    return sum(nums)

print(add(5,7,4,2))

def calculate(n,**kwargs):
    """
    This function takes an integer n as an argument and an arbitrary number of keyword arguments.
    It returns the sum of the values of the keyword arguments multiplied by n.
    >>> calculate(2, x=3, y=4, z=5)
    30
    >>> calculate(3, a=2, b=3, c=4)
    27
    """
    return sum(kwargs.values()) * n
    