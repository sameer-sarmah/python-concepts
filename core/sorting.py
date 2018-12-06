from modules.person import Person
sameer=Person("sameer",29,False)
mayuri=Person("mayuri",29,False)
panda=Person("panda",29,False)
pari=Person("pari",29,False)
sameer.printDetails()
sameer.printDetails()
print(sameer.__eq__(mayuri))
print(sameer > mayuri)
print(str(sameer))

def personKey(person):
    return person.name

persons=[sameer,mayuri,panda,pari]

sortedPersons=sorted(persons,key=personKey,reverse=False)

for person in sortedPersons:
    print(person.name)

persons.sort(key=personKey)

for person in persons:
    print(person.name)

print(__name__)