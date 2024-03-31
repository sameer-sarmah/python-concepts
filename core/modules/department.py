class Department:
    def __init__(self,dptName: str):
        self.name = dptName

    # Getter function
    @property
    def name( self ) -> str:
        return self._name

    # Setter function
    @name.setter
    def name( self, dptName: str ):
        self._name = dptName


department = Department("Finance")
print(department.name)
department.name = "Engineering"
print(department.name)