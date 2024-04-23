count=0
l = [0, 2, 3, 4, 1, 2, 3, 5, 6]
for i in l:
    for j in l:
        if(i==j):
            count+=1
    if(count>1):
        print(i)
        break
