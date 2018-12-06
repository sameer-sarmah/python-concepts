


class Person:

    def __init__(self, nameArg, ageArg, isMarriedArg):
        self.name = nameArg
        self.age = ageArg
        self.married = isMarriedArg

    def printDetails(self):
        print(f"name is {self.name} age  {self.age}")

    def __eq__(self, o: object) -> bool:
        if(self.name == o.name and self.age == o.age):
            return True
        else:return False

    def __ne__(self, o: object) -> bool:
        ne=not self.__eq__(self, o)
        return ne

    def __str__(self) -> str:
        return f"name is {self.name}, age is {self.age}"

    def __hash__(self) -> int:
        return super().__hash__()

    def __gt__(self, other):
        if(self.name > other.name):
            return True
        else:return False

    def __lt__(self, other):
        lt=not self.__lt__(self, other)
        return lt

    def __ge__(self, other):
        isEqual=self.__eq__(self, other)
        isGreater=self.__gt__(self, other)
        return isEqual or isGreater

    def __le__(self, other):
        isEqual=self.__eq__(self, other)
        isLesser=not self.__gt__(self, other)
        return isEqual or isLesser

    def __copy__(self):
        return Person(nameArg=self.name,ageArg=self.age,isMarriedArg=self.married)

    def __deepcopy__(self, memodict={}):
        return self.__copy__(self)

print(__name__)