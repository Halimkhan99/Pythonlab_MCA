a=int(input("Enter a number : "))
x=a
y=0
while(a>0):
    r = a % 10
    y = y * 10 + r
    a = a // 10
if(x==y):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
