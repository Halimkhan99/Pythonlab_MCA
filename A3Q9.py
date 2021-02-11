Number = int(input(" Please Enter The Number: "))
for num in range(1, Number + 1):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num,end=" ")
