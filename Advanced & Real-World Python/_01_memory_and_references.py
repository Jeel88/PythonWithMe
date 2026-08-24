x = 10
y = x

print(id(x))
print(id(y))


x = 10
y = x

print(x)
print(y)

x = 10
y = x

x = 20

print(x)
print(y)


a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)