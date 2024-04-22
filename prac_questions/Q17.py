def check(string):
    a=0
    d=0
    for l in string:
        if(l.isdigit()):
            d+=1
        if(l.isalpha()):
            a+=1
    
    return a, d


string=input("Enter the string: ")
print(check(string))


