from collections import deque,OrderedDict,defaultdict
numbers = deque([1,2,3,4,5,6])
print(numbers.pop())
print(numbers.popleft())


my_dict = {'name': 'John', 'country': 'Germany'}
linkedMap = OrderedDict(my_dict)
for key,value in linkedMap.items():
    print(f"{key} -> {value}")
print(my_dict.get('profession','Engineer'))
def default():
    return '';
#mapWithDefaultValue= defaultdict(lambda : 'default',my_dict)
mapWithDefaultValue= defaultdict(str,my_dict)
print(mapWithDefaultValue.get('profession'))
print(mapWithDefaultValue.get('country'))

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
motorcycles.remove('honda')
#del motorcycles[0]
motorcycles.pop(0)
print(motorcycles)

numbers = list(range(1, 6))
maxNumber = max(numbers)
minNumber = min(numbers)
numbersTillIndex3 = numbers[0:4]
print(numbersTillIndex3)