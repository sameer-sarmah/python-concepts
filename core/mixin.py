from abc import ABC
from typing import List


# ABC signals these are traits/mixins — NOT meant to be instantiated standalone
# Python has no 'trait' keyword, so ABC is the closest convention
class SportsCar(ABC):
    def sportify( self ):
        self.sporty = True
        if self.features is not None and isinstance(self.features,List):
            self.features += ['High power', 'High torque']
            print(f"Up for a adrenalin ride")


class LuxuryCar(ABC):
    def luxurify( self ):
        self.comfy = True
        if self.features is not None and isinstance(self.features,List):
            self.features += ['Leather upholstery', 'premium features']
            print(f"Up for a comfortable ride")


class Jaquar(LuxuryCar):

    def __init__( self ):
        self.features = []

    def getFeatures( self ):
        print(f"Up for a luxurious and comfortable ride.Features={self.features}")

class Ferrari(SportsCar):

    def __init__( self ):
        self.features = []

    def getFeatures( self ):
        print(f"Up for a adrenalin filled ride.Features={self.features}")

class LuxuryFerrari(SportsCar, LuxuryCar):   # ← mixes in BOTH behaviours
    def __init__(self):
        self.features = []

    def getFeatures(self):
        print(f"Up for a luxurious adrenalin ride. Features={self.features}")


jaquar = Jaquar()
jaquar.luxurify()
jaquar.getFeatures()

ferrari = Ferrari()
ferrari.sportify()
ferrari.getFeatures()

luxury_ferrari = LuxuryFerrari()
luxury_ferrari.sportify()    # from SportsCar mixin
luxury_ferrari.luxurify()    # from LuxuryCar mixin
luxury_ferrari.getFeatures()
