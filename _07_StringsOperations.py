name="jeel"
language="python"
print(name)
print(language)
 #conctenation
fullName= name + " Savaliya"
print(fullName)
#fprinting
print(f"My name is {name}")
print(f"I am Learning {language}")
 #string len
print(len(name))
# Indexing
print(fullName[0])
print(fullName[1])
print(fullName[-1])
# Slicing
print(fullName[0:3])
print(fullName[:3])
print(fullName[2:])
print(fullName[:])
print(fullName[::-1])
#string methods
text="hello python"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

print(text.replace("hello","bye"))

print(text.startswith("hello"))
print(text.endswith("python"))
# Split string
words = text.split()
print(words)
