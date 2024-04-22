def find_missing_numbers(set1, set2):
    missing_in_set2 = set1 - set2
    missing_in_set1 = set2 - set1
    return missing_in_set2, missing_in_set1


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
missing_in_set2, missing_in_set1 = find_missing_numbers(set1, set2)

print("First set:", set1)
print("Second set:", set2)
print("Missing numbers in the second set compared to the first:", missing_in_set2)
print("Missing numbers in the first set compared to the second:", missing_in_set1)
