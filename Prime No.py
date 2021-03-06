p = int(input("Enter a number : "))
if p>1:
    for i in range(2,p):
        if (p%i)==0:
            print(p,"Not Prime number")
            break
        else:
            print(p,"Prime number")
else:
    print(p,"Not Prime number")
