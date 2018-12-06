from modules.person import Person
import copy
sameer=Person("sameer",29,False)
cloneOfSameer=copy.copy(sameer)
print(str(cloneOfSameer))

print(sameer is cloneOfSameer)
print(sameer == cloneOfSameer)