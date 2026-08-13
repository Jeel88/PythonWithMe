a=int(input("Enter Number For Sum"))
ans=0
while a>0:
    digits=a%10
    ans += digits
    a=a//10
print(ans)    

b=input("Enter Ur Numbers")
total=0
for i in b:
    total+=int(i)
    print(i)
print(total)
