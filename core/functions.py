import functools
import types
from typing import Callable
from modules.person import Person

def isEven( num: int ) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False


def add( num1: int, num2: int ) -> int:
    return num1 + num2


arr = [1, 2, 3, 4]

evenNums = filter(isEven, arr)

print("even numbers are")
for num in evenNums:
    print(num)

# multiple statements or expressions NOT supported
double = lambda num: 2 * num
print(isinstance(double,types.LambdaType))  # Output: True
doubledArr = map(double, arr)
print("doubled numbers are")
for num in doubledArr:
    print(num)

sum = functools.reduce(add, arr, 0)
print(f"the sum of the array is {sum}")

set = {"a", "b", "c", "d"}
print("uppercased letters are")


def toUpperCase( string ):
    if (isinstance(string, str)):
        return string.upper()


upperCased = map(toUpperCase, set)

for string in upperCased:
    print(string)


def funAsReturnValue():
    return add;


def funcAsArg( fun : Callable[[int,int], int], num1, num2 ):
    return fun(num1, num2)


print(funcAsArg(funAsReturnValue(), 1, 2))
fun = add
print(funcAsArg(fun, 10, 20))


def lambdaAsReturnValue():
    return double;


def lambdaAsArg( lambdaReference : Callable[[int], int], number ):
    return lambdaReference(number)


print(lambdaAsArg(lambdaAsReturnValue(), 1))
print(isinstance(isEven, types.FunctionType))  # Output: True


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def double(numbers):
    for index,number in enumerate(numbers):
        numbers[index]=2*number

double(numbers[:]) # pass a copy of the list
print(numbers) # original list is unchanged
double(numbers)
print(numbers)

def personNames( *names ):
    if names is not None:
        for name in names:
            print(name)


personNames("sameer", "mayuri")
personNames(None)


def personWithGender( **namesWithGender ):
    print(type(namesWithGender))
    for (name, gender) in namesWithGender.items():
        print(f"name is {name} and gender is {gender}")


personWithGender(sameer="male", mayuri="female")

