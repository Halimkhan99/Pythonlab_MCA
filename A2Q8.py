print('Enter marks of five subjects')
s1, s2, s3, s4, s5 = int(input()), int(input()), int(input()),int(input()),int(input())
total = s1 + s2 + s3 + s4 + s5
print('total = ',total)
avg = total / 5
print('avg =',avg)
if (avg>=90):
    print ('O')
elif(80<=avg<=89):
    print('E')
elif(70<=avg<=79):
    print('A')
else :
    print('B')
