from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*arg):
        print(f"operation performed is {func.__name__} ,result is {func(arg[0])}")

    return wrapper

def decoratorWithArgs(details):
    def decoratorBase(func):

        @wraps(func)
        def wrapper(*args):
            num = args[0]
            print(f"operation performed is {func.__qualname__} ,result is {func(num)}, details about decorator is {details}")

        return wrapper
    return decoratorBase

def classDecorator(klass):
    items=klass.__dict__.items()
    for pair in items:
        if isinstance(pair, tuple):
            (propertyName, propertyValue)=pair
            print(f"property name '{propertyName}' property value '{propertyValue}'")
            if callable(propertyValue):
                setattr(klass, propertyName, decorator(propertyValue))
    return klass


import math

number = 4.5
factorial_of=5


ceiling=decorator(math.ceil)
factorial=decorator(math.factorial)

@decorator
def sqrt(num):
    return math.sqrt(num)


ceiling(number)
sqrt(number)
factorial(factorial_of)




@decoratorWithArgs(details="This function calculates sin of a number")
def sin(num):
    return math.sin(num)

sin(90)
# help(ceiling)
# help(sqrt)

