def max_subsequence_sum(lst):
    if not lst:
        return 0

    
    current_sum = 0

    for num in lst:
        current_sum = max(current_sum, current_sum + num)
        

    return current_sum

# Test the function
my_list = [1, -2, 3, -4, 5, -6, 7]
print("Maximum sum sub-sequence in the list:", max_subsequence_sum(my_list))
