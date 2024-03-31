from enum import Enum


def add( num1, num2 ):
    return num1 + num2


# Python does not have constants
# Python doesn’t have a dedicated syntax for enums.
class Season(Enum):
    WINTER = 'WINTER'
    SPRING = 'SPRING'
    SUMMER = 'SUMMER'
    FALL = 'FALL'


summer = Season.SUMMER

print(add(1, 2))
name = "sameer"
message = f"hello {name}"
print(message)
chars = name.split("m")
print(chars)
arr = [1, 2, 3, 4]

index = 0
while index < len(arr):
    print(f"index is {index}")
    print(arr[index])
    index += 1

my_tuple = (1, "Hello", 3.4)
print(my_tuple)

my_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_dict['name'])

my_dict['key'] = 'value'
print(my_dict['key'])

name = "asd"
print(name.isdecimal())
print(name.islower())


def person( name, age=20 ):
    print(f"name is {name} and age is {age}")


person(age=25, name="mayuri")
person(name="mayuri")


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

from cloning import Person

mayuri = Person("Mayuri", 29, False)
mayuri.printDetails()

for (key, value) in mayuri.__dict__.items():
    print(f"property name '{key}' property value '{value}'")
