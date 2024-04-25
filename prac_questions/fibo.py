def fibo(num):
    if(num<=0):
        return 1
    
    return fibo(num-2)+fibo(num-1)

print(fibo(6))