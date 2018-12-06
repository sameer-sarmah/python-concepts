class Sample:
    pass

sample=Sample
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

setattr(sample,"add",add)
print(callable(sample.__dict__['add']))
print(sample.add(2,3))
setattr(sample,"add",None)
print(getattr(sample,"add"))
sample.sub=sub
print(sample.sub(20,3))

