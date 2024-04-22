#Write a program to find GCD of two numbers. Write a program to find a Fibonacci of a number
#Write a program to find a factorial of a number.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 48
num2 = 18
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b



def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

num = 5
print("Factorial of", num, "is:", factorial(num))
num = 10
print("Fibonacci of", num, "is:", fibonacci(num))
num1 = 48
num2 = 18
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))

