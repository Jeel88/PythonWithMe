number=int(input("Enter Number:"))
if number<2:
    print("Not Prime")
else:
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False
            break
    if is_prime:
        print("It is Prime")
    else:
        print("Not Prime")        