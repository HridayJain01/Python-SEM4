l1=[1,2,3,4,5,6,7,8]
l2=[1,2,3,4,4,4,4,9]

l1=set(l1)
l2=set(l2)
result=[]

for i in l1:
    for j in l2:
        if(i==j):
            result.append(i)


print(result)
