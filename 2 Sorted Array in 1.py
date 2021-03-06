def m(a,b):
    i=0
    j=0
    len1=len(a)
    len2=len(b)
    newarr=[]
    while((i<len1)and(j<len2)):
        if(a[i]<b[j]):
            newarr.append(a[i])
            i+=1
        else:
            newarr.append(b[j])
            j+=1
    while(i<len1):
        newarr.append(a[i]) 
        i+=1
    while(j<len2):
        newarr.append(b[j])
        j+=1
    return newarr

a=[11,15,19,21]
b=[12,13,16,17,18]
print("First Array: ",a)
print("Second Array: ",b)
newarr=m(a,b)
print("Merged Array: ",newarr)
