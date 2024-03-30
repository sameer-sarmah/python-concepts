import math

class Decorator:
    def __init__( self, func ):
        self.func = func
        print(f"decorator constructor called with argument {self.func.__qualname__}")

    def __call__( self, number ):
        print(f"decorating function {self.func.__qualname__}")
        return self.func(number)


@Decorator
def logBase10( num ):
    return math.log10(num)


print(logBase10(100))


# In a decorator with arguments the function reference is not passed in the constructor
class DecoratorWithArg:
    def __init__( self, description ):
        self.description = description

    def __call__( self, func ):
        def wrapper( number: int ):
            print(f"decorating function {func.__name__} , description about decorator is '{self.description}'")
            func(number)
        return wrapper


@DecoratorWithArg(description="This function calculates log base 2 of a number")
def logBase2( num ):
    return math.log2(num)


print(logBase2(8))


