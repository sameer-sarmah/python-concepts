def printDetailsfromList(details):
    print("unpacking list")
    age, height = details
    print(f"age in years is {age} height in cms is {height}")


details = [25, 173]
printDetailsfromList(details)


def printDetailsfromTuple(details):
    print("unpacking tuple")
    age, height = details
    print(f"age in years is {age} height in cms is {height}")


details = (25, 173)
printDetailsfromTuple(details)


def printDetailsfromDictionary(details):
    print("unpacking dictionary")
    age, height = details
    print(f"age in years is {age} height in cms is {height}")


details = {'age': 25, 'height': 173}
printDetailsfromDictionary(details)
