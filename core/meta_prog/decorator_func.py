


def decorator( func ):
    def wrapper( number: int ):
        print(f"decorating function {func.__name__}")
        return func(number)

    return wrapper


import math

number = 4.5
factorial_of = 5

decoratedCeiling = decorator(math.ceil)
print(decoratedCeiling(number))

decoratedFactorial = decorator(math.factorial)
print(decoratedFactorial(factorial_of))

@decorator
# It means the sqrt function would be decorated by decorator function
#it is similar to writing
#decoratedSqrt = decorator(sqrt)
#decoratedSqrt(number)

def sqrt( num ):
    return math.sqrt(num)
print(sqrt(number))


