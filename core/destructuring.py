from typing import List


def printDetailsfromList( details ):
    print("unpacking list")
    age, height = details
    print(f"age in years is {age} height in cms is {height}")


details = [25, 173]
printDetailsfromList(details)


def printDetailsfromTuple( details ):
    print("unpacking tuple")
    age, height = details
    print(f"age in years is {age} height in cms is {height}")


details = (25, 173)
printDetailsfromTuple(details)


def printDetailsfromDictionary( details ):
    print("unpacking dictionary")
    ageKey, heightKey = details
    print(f"age in years is {details[ageKey]} height in cms is {details[heightKey]}")
    age, height = details.values()
    print(f"age in years is {age} height in cms is {height}")



details = {'age': 25, 'height': 173}
printDetailsfromDictionary(details)

# destructuring of fields in an object(similar to JS) is not supported

head, *middle, tail = [1, 2, 3, 4, 5]
print(head)  # 1
print(middle)  # [2, 3, 4]
print(tail)  # 5
print(isinstance(middle, List))
