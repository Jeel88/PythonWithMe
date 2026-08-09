age = 20
#if
if age >= 18:
    print("You are an adult")
#if-else
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
#if-elif-else
marks = 82
if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)

#multiple conditions
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")