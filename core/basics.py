from enum import Enum
import time,datetime,logging,os
import random
logging.basicConfig(level=logging.INFO)

startTime = time.time();

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

nameAge = ("Adam",30)
name = nameAge[0]
print(name)

my_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_dict['name'])

my_dict['key'] = 'value'

print(my_dict['key'])
#create a dictionary employee to department in a company
employeeToDepartment = {'sameer': 'IT', 'mayuri': 'Finance'}
for (employee, department) in employeeToDepartment.items():
    print(f"employee is {employee} and department is {department}")

for employee in employeeToDepartment.keys():
    department = employeeToDepartment[employee]
    print(f"employee is {employee} and department is {department}")

name = "asd"
print(name.isdecimal())
print(name.islower())

def person( name, age=20 ):
    print(f"name is {name} and age is {age}")


person(age=25, name="mayuri")
person(name="mayuri")




from cloning import Person

mayuri = Person("Mayuri", 29, False)
mayuri.printDetails()

for (key, value) in mayuri.__dict__.items():
    print(f"property name '{key}' property value '{value}'")


currentUtc = datetime.datetime.now(datetime.timezone.utc)
currentUtcStr = currentUtc.strftime("y-M-d'T'H:m:s.SSSZ")
print(currentUtcStr)

endTime = time.time();
logging.info(f"time elapsed={endTime - startTime}")
logger = logging.getLogger('BasicModule')
java_home = os.getenv('JAVA_HOME')
logger.info(f"os={os.name},JavaHome={java_home}")

universe_age = 14_000_000_000
x, y, z = 0, 0, 0

ageInString = "30"
age = int(ageInString)
print(age)

price = 99.99
priceInString = str(price)
print(priceInString)


def isPrime( number ):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def isEven( num: int ) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False

numbers = range(1,100)
for number in numbers:
    if isEven(number):
        continue
    elif(isPrime(number) and number>50 ):
        print(f"prime number greater than 50 is {number}")
        break;
    else:
        pass


