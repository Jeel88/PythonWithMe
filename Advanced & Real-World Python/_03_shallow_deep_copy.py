import copy

original = [[1, 2], [3, 4]]
copied = copy.deepcopy(original)

copied[0].append(100)

print(original)
print(copied)

# Shallow copy
copied = original.copy()