def callmeback(n):
    if n == 0 :
        print("It is Zero")
        return
    print(n)
    callmeback(n-1)
callmeback(5)    