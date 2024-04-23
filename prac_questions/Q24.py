def kth_smallest_element(lst, k):
    sorted_list = sorted(lst)
    if k > len(sorted_list) or k <= 0:
        return None
    return sorted_list[k - 1]

my_list = [4, 2, 7, 1, 9, 3]
k = 3
print(f"The {k}th smallest element in the list:", kth_smallest_element(my_list, k))
