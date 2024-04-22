def third_largest(numbers):
    wd = set(numbers)  
    un = list(wd) 
    if len(un) < 3:
        return "List doesn't contain enough elements"
    un.sort
    return un[len(un)-3] 

numbers = [1, 3, 5, 7,9, 5, 7, 3, 1]  
print("Original list:", numbers)
print("Third largest number:", third_largest(numbers))
