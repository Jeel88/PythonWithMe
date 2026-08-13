a=int(input("enter number"))
org=a
reverse=0
while a>0:
    digit=a%10
    reverse=reverse*10+digit
    a//=10
if org == reverse:
    print("The number is a Palindrome")
else:
    print("The number is not a Palindrome")    