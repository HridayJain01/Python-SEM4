import matplotlib.pyplot as plt
import numpy as np


'''print(help(plt))'''
array=[200,182,433,649]

#plt.pie(array)
#plt.scatter(array,array)
#plt.(array,array)
#plt.show()

x=[1,2,3,4,5,6,8,9,4,2,4,2]
y=[1,5,6,2,4,6,3,5,3,5,4,2]
colour=["r","g","b"]
plt.subplot(3,2,1)
plt.plot(x,y,color="black")

plt.subplot(3,2,1)
plt.scatter(x,y,color="red")

plt.subplot(3,2,2)
plt.scatter(x,y)

plt.subplot(3,2,2)
plt.scatter(x,y,color="green")
plt.scatter(y,x,color="black")

plt.subplot(3,2,3)
plt.pie(x)
plt.legend(x)
plt.subplot(3,2,4)
plt.bar(x,y)
plt.bar(y,x,color="black")
plt.subplot(3,2,5)
plt.barh(x,y)
plt.xlabel("100")
plt.legend(x,y)

plt.subplot(3,2,6)
plt.hist(x)

plt.show()

