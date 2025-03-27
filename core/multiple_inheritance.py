class Color:
    def __init__(self,color):
        self.color=color

    def getColor(self):
        print(f"I am {self.color}")

class Shape:
    def __init__(self,shape):
        self.shape=shape

    def getShape(self):
        print(f"I am a {self.shape}")

class ColoredRectangle(Shape,Color):
    def __init__(self,shape,color):
        Color.__init__(self,color)
        Shape.__init__(self, shape)

    def details(self):
        print(f"Shape={self.shape},Color={self.color}")


red=Color("red")
rectangle=Shape("rectangle")
redRectangle=ColoredRectangle(shape="rectangle",color="red")
redRectangle.getColor()
redRectangle.getShape()
redRectangle.details();
############################################################################################
class Car:
    mileage=20
    power = 100

    def __init__(self,mileage,power,brand):
        self.brand=brand
        self.mileage=mileage
        self.power=power
    def getFeatures(self):
        pass

class SportsCar(Car):
    sporty=True
    mileage = 10
    power = 400

    def __init__( self, mileage, power, brand ):
        super().__init__(mileage, power, brand)
    def getFeatures(self):
        print(f"Up for a adrenalin ride")


class LuxuryCar(Car):
    mileage = 15
    power = 200
    comfy = True

    def __init__( self, mileage, power, brand ):
        super().__init__(mileage, power, brand)
    def getFeatures(self):
        print(f"Up for a comfortable ride")

class Jaquar(SportsCar,LuxuryCar):
    def getFeatures(self):
        print(f"Up for a adrenalin and comfortable ride")


print(Jaquar.comfy)
print(Jaquar.sporty)
############################################################################################

from modules.person import Person

class WhiteCollar:
    def specialization(self):
        pass


class Engineer(WhiteCollar,Person):

    def __init__(self,name, age, isMarried,speciality):
        Person.__init__(self, name, age,isMarried)
        self.speciality=speciality

    def specialization(self):
        print(f"I build {self.speciality}")

    def printDetails(self):
        print(f"name is {self.name} ,age is {self.age}, speciality is {self.speciality}")


mayuri=Engineer(name="Mayuri",age=29,isMarried=False,speciality="Software")
mayuri.specialization()
mayuri.printDetails()

for (key,value) in mayuri.__dict__.items():
    print(f"property name '{key}' property value '{value}'")

print(Engineer.__mro__)
