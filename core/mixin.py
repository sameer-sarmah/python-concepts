from typing import List


class SportsCar:
    def sportify( self ):
        self.sporty = True
        if self.features is not None and isinstance(self.features,List):
            self.features += ['High power', 'High torque']
            print(f"Up for a adrenalin ride")


class LuxuryCar:
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

jaquar = Jaquar()
jaquar.luxurify()
jaquar.getFeatures()

ferrari = Ferrari()
ferrari.sportify()
ferrari.getFeatures()