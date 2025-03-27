from typing import List

names = ["sameer", "mayuri"]
print("sameer" in names)
print("Sameer" not in names)

def printElements( elements=[] ):
    if (isinstance(elements, List) and len(elements) > 0):
        for element in elements:
            print(element)
    else:
        print("elements is empty")


printElements(names)
printElements([])
printElements(None)


def isEven( num: int ) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False


print(isEven(2))
