def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)

# Test the function
num = 5
print("Sum of non-negative integer up to", num, ":", sum_recursive(num))
