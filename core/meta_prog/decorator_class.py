class Decorator:
    def __init__(self,func):
        self.func=func

    def __call__(self, number):
        print(f"operation performed is {self.func.__qualname__} ,result is {self.func(number)}")

#In a decorator with arguments the function reference is not passed in the constructor
class DecoratorWithArg:
    def __init__(self,details):
        self.details=details

    def __call__(self, func):
        def wrapper(*args):
            num=args[0]
            print(f"operation performed is {func.__qualname__} ,result is {func(num)}, details about decorator is {self.details}")

        return wrapper

import math

@Decorator
def logBase10(num):
    return math.log10(num)

logBase10(100)

@DecoratorWithArg(details="This function calculates log base 2 of a number")
def logBase2(num):
    return math.log2(num)

logBase2(8)

class ClassDecorator:
    def __init__(self,func):
        self.func=func

    def __call__(self, number):
        print(f"operation performed is {self.func.__qualname__} ,result is {self.func(number)}")