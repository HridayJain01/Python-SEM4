def palin(num):
    n=num
    rev = 0
    rem=0
    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n //= 10

    return rev == num


num=int(input("Enter a number: "))
print(palin(num))
