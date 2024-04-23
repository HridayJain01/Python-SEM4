#trying out lambda for different usecases

x="11 2 odd"



digits=list(map(int,filter(lambda x:x.isdigit(),x.split())))
print(digits)
odd_parts=list(map(int,filter(lambda digits: digits%2!=0,digits)))
print(odd_parts)


l1=[(1,2,3,4,5),(6,7,8,9),(10,11)]
total=sum(map(lambda x:sum(x),l1))
print(total)


