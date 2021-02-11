def fibonacci():
    f1 = 0
    f2 = 1
    n = int(input("Enter The Term : "))
    if n < 1:
        return
    for x in range(1,n):
        print(f2,end = " ")
        f = f1 + f2 
        f1 = f2
        f2 = f
if __name__ == "__main__":
    fibonacci()
