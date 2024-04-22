list=[0,1,2,3,4,5,6,7,8,9]
list2=[9,8,7,6,5,4,3,2,1,0]
flag=True
for i in range(len(list)) :
    if list[i] != list2[len(list)-1-i]:
        flag=False
        break
        
if(flag):
    print("The two lists are equal")
else:
    print("The two lists are not equal")


