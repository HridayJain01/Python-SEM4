#Write a program to find a minimum of three numbers. Write a program to check if the given
#strings are anagram or not. Write a program to check if the given number is Armstrong or not.



def minimum_of_three(a, b, c):
    return min(a, b, c)

num1 = 10
num2 = 5
num3 = 8
print("Minimum of", num1, ",", num2, ", and", num3, "is:", minimum_of_three(num1, num2, num3))

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


string1 = "listen"
string2 = "silent"
print("Are", string1, "and", string2, "anagrams?", is_anagram(string1, string2))

def is_armstrong(num):
    n=0
    sum=0
    while(num!=0):
        n=n%10
        sum=sum+(n*n*n)
        num/=10
    return sum == num



number = 153
print(number, "is an Armstrong number?", is_armstrong(number))


