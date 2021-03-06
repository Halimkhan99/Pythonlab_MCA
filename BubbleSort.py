def bs(l):
    leng=len(l)-1
    s=False
    while not s:
        s=True
        for i in range(0,leng):
            if l[i]>l[i+1]:
                s=False
                l[i],l[i+1]=l[i+1],l[i]
    return l
print(bs([4,6,8,3,2,5,7,8,9]))