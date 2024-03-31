from collections import deque,OrderedDict,defaultdict
numbers = deque([1,2,3,4,5,6])
print(numbers.pop())
print(numbers.popleft())


my_dict = {'name': 'John', 'country': 'Germany'}
linkedMap = OrderedDict(my_dict)
for key,value in linkedMap.items():
    print(f"{key} -> {value}")
def default():
    return '';
#mapWithDefaultValue= defaultdict(lambda : 'default',my_dict)
mapWithDefaultValue= defaultdict(str,my_dict)
print(mapWithDefaultValue.get('profession'))
print(mapWithDefaultValue.get('country'))