def kth_largest_element(lst, k):
    sorted_list = sorted(lst, reverse=True)
    if k > len(sorted_list) or k <= 0:
        return None
    return sorted_list[k - 1]

my_list = [4, 2, 7, 1, 9, 3]
k = 3
print(f"The {k}th largest element in the list:", kth_largest_element(my_list, k))
