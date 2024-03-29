from core.meta_prog.decorator_class import ClassDecorator
from core.meta_prog.decorator_func import decorator
from core.modules.person import Person
# type is class ,classes and other types are instances of class type
print(type(int))
print(type(str))
print(type(type(decorator)))
print(type(ClassDecorator))
print(type(type))


def __init__(self, name, age, isMarried):
    Person.__init__(self, name, age, isMarried)


PersonSubclass = type('PersonSubclass', (Person,), {__init__:__init__})
person=PersonSubclass("sameer",28,False)
print(PersonSubclass.__name__)
print(isinstance(person,Person))