def find_permutations(x):
    if len(x) == 0:
        return [[]]
    perm_list = []
    for i in range(len(x)):
        current_element = x[i]
        remaining_elements = []
        for j in range(len(x)):
            if j != i:
                remaining_elements.append(x[j])
        for p in find_permutations(remaining_elements):
            perm_list.append([current_element] + p)
    return perm_list

x = [1, 2, 3]
print("All permutations of the list:", find_permutations(x))
