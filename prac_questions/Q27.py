def find_union(list1, list2):
    
    set1 = set(list1)
    set2 = set(list2)
    union = set1.union(set2)
    return list(union)

def find_intersection(list1, list2):
    
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    return list(intersection)


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("Union of the two lists:", find_union(list1, list2))
print("Intersection of the two lists:", find_intersection(list1, list2))
