def p1(): 
    print("Pattern 1 \n")
    n=int(input("Enter The Number : "))
    for i in range(1,n+1):
        print("* "*i)
def p2():
    print("\nPattern 2 \n")
    n=int(input("Enter The Number : "))
    for i in range(n,0,-1):
        print("A "*i)
def p3():
    print("\nPattern 3 \n")
    n=int(input("Enter The Number : "))
    for i in range(n,0,-1):
        print("  "*(n-i)+"A "*i)
if __name__=="__main__":
    p1()
    p2()
    p3()
