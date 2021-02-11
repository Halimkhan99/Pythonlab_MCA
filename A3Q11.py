def p1():
    print("Pattern 1:\n")
    n=5
    for i in range(1,n+1):
        print(" "*(n-i)+"O "*i)
def p2():
    print("\nPattern 2:\n")
    n=5
    for i in range(n,0,-1):
        print(" "*(n-i)+"O "*i)
def p3():
    print("\nPattern 3:\n")
    n=4
    v=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(v,end=" ")
            v+=1
        print("\n")
if __name__ == "__main__":
    p1()
    p2()
    p3()
