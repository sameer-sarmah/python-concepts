
class NumberOperatorOverloading:
    def __init__(self,value):
        assert isinstance(value,int) or isinstance(value,float)
        self.value=value

    def __add__(self, other):
        return NumberOperatorOverloading(self.value+other.value)

    def __mul__(self, other):
        return NumberOperatorOverloading(self.value*other.value)

    def __sub__(self, other):
        return NumberOperatorOverloading(self.value-other.value)

    def __truediv__(self, other):
        assert other.value != 0
        return NumberOperatorOverloading(self.value/other.value)

    def __str__(self):
        return f"value is {self.value}"

four=NumberOperatorOverloading(4)
five=NumberOperatorOverloading(5)

print(four + five)
