def longest_length(nums):
    maxl = 0
    if len(nums) == 0:
        return maxl
    c = 1

    prev = nums[0] 

    for i in nums:
        if i > prev:  
            c += 1
        else:
            c = 1  
        maxl = max(maxl, c)
        prev = i 
    return maxl

sequence = [10, 9, 2, 5, 3, 7, 101, 18]
print("Length of the longest increasing sub-sequence:", longest_length(sequence))
