def person():
    name: str = None

    def getName():
        return name

    def setName( nameArg: str ):
        nonlocal name
        name = nameArg

    return {'setName': setName, 'getName': getName}


sameer = person()
setName,getName = sameer.values()
setName('sameer')
print(getName())