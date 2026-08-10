fruits=["apple","banana","cherry","strawberry"]
print(fruits)
fruits.append("pineapple")
print(fruits)
fruits.insert(1,"orange")
print(fruits)
fruits.extend(["grapes","watermellon"])
print(fruits)

fruits.remove("pineapple")
print(fruits)

popf=fruits.pop()
print("poped fruits last: ",popf)
popMid=fruits.pop(2)
print("poped fruits AT Index: ",popMid)

print(fruits.index("cherry"))

numbers = [10, 20, 10, 30, 10]
print(numbers.count(10))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.clear()
print(numbers)