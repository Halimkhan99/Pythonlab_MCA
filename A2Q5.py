n=input("Enter a no.:")
if(n>='A' and n<'Z') or (n>='a' and n<'z'):
    print("Not the integer")
else:
    l=len(n)
    if(l==2):
        print("No is two digit")
    else:
        print("No is not two digit")