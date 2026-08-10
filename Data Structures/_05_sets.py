fruits={"Apple","banana","cherry","strawberry"}
print(fruits)
numbers={10,20,20,30,60,80,40,22}
print(numbers)
fruits.add("grapes")
print(fruits)
fruits.update(["pineapple","watermellon"])
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.discard("Apple")
print(fruits)
print(len(fruits))

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
#union
print(a | b)

#intersection
print(a & b)

#difference
print(a - b)
#symmetric difference
print(a ^ b)
