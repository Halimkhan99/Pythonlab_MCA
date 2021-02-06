print('Enter marks of four subjects')
s1, s2, s3, s4 = int(input()), int(input()), int(input()), int(input())
total = s1 + s2 + s3 + s4
print('total = ',total)
avg = total / 4
print('Your Grade =',avg)
if (avg>=40):
    print ('Congratulation You have Passed ')
else :
    print('You have Failed')