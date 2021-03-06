n1 = int(input("Enter first Integer : "))
n2 = int(input("Enter Second Integer : "))
if n1 > n2:
    smaller = n2
else :
    smaller = n2
for i in range(1, smaller+1):
    if((n1 % i == 0) and (n2 % i == 0)):
        hcf = i 
print("The H.C.F. is = ", hcf)
