class CustomMetaClass(type):
    def __new__(cls, name,baseClasses,dictionary):
        print(f"The class name is {name} and inherits from {baseClasses}")
        return super().__new__(cls, name,baseClasses,dictionary)

class MetaClassDemo(metaclass=CustomMetaClass):
    pass

class MetaClassDemoSubclass(MetaClassDemo):
    pass

obj=MetaClassDemoSubclass()