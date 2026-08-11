def double(x):
    return x*2
numbers=[1,2,3,4,5]
Lnum=list(map(double,numbers))
print(Lnum)

result = list(map(lambda x: x * 2, numbers))
print(result)