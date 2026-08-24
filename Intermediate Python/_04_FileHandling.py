file = open("_03_Pip.txt", "r")
content = file.read()
print(content)
file.close()

# with open("_03_Pip.txt", "w") as file:
#     file.write("Hello Python")


# with open("_03_Pip.txt", "a") as file:
#     file.write("\nLearning File Handling")


# with open("_03_Pip.txt", "r") as file:
#     for line in file:
#         print(line.strip())