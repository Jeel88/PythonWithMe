# ==========================================
# Regular Expressions (Regex)
# ==========================================

import re


# ------------------------------------------
# 1. re.search()
# ------------------------------------------

text = "My phone number is 9876543210"

result = re.search(r"\d+", text)

if result:
    print("Search:", result.group())


# ------------------------------------------
# 2. re.findall()
# ------------------------------------------

text = "I have 10 apples and 25 oranges"

numbers = re.findall(r"\d+", text)

print("Find all:", numbers)


# ------------------------------------------
# 3. re.match()
# ------------------------------------------

text = "Python is amazing"

result = re.match(r"Python", text)

if result:
    print("Match found")


# ------------------------------------------
# 4. Check exactly 10 digits
# ------------------------------------------

phone = "9876543210"

if re.fullmatch(r"\d{10}", phone):
    print("Valid phone number")
else:
    print("Invalid phone number")


# ------------------------------------------
# 5. Useful Regex Patterns
# ------------------------------------------

text = "Jeel is 20 years old"

# \d → digit
print(re.findall(r"\d", text))

# \d+ → one or more digits
print(re.findall(r"\d+", text))

# \w → letter, digit or underscore
print(re.findall(r"\w+", text))

# \s → whitespace
print(re.findall(r"\s", text))


# ------------------------------------------
# 6. re.sub() - Replace text
# ------------------------------------------

text = "Python is difficult"

new_text = re.sub(r"difficult", "easy", text)

print(new_text)


# ==========================================
# Common Patterns
# ==========================================

# \d     → digit
# \w     → letter, digit, underscore
# \s     → whitespace
# .      → almost any character
# +      → one or more
# *      → zero or more
# ?      → zero or one
# ^      → start of string
# $      → end of string
# {10}   → exactly 10 occurrences