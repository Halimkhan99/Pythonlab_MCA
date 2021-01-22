# Python program to find simple interest 
#1
P = float(input("Enter the principal amount : "))
N = float(input("Enter the number of years : "))
R = float(input("Enter the rate of interest : "))
#2
I = (P * N * R)/100
print("Simple interest : {}".format(I))