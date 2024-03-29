import functools


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


def funcAsArg( fun, num1, num2 ):
    return fun(num1, num2)


print(funcAsArg(funAsReturnValue(), 1, 2))
fun = add
print(funcAsArg(fun, 10, 20))


def lambdaAsReturnValue():
    return double;


def lambdaAsArg( lambdaReference, number ):
    return lambdaReference(number)


print(lambdaAsArg(lambdaAsReturnValue(), 1))
