number=int(input("Enter Numberto Rev:"))
revnumber=0
while number>0:
    digit=number%10
    revnumber=revnumber*10+digit
    number=number//10
print(revnumber)    

num=9832743
print(str(num)[::-1])