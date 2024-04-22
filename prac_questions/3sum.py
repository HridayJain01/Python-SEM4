def find_combinations(no, target):
    result = []
    no = len(n)
    for i in range(no):
        for j in range(i+1, no):
            for k in range(j+1, no):
                s = [n[i], n[j], n[k]]
                if sum(s) == target:
                    result.append(tuple(s))
    return result


n = [2, 4, 6, 3, 7, 1]
target = 10
print("Original list of n:", n)
print("Target number:", target)
print("Unique combinations adding up to the target:", find_combinations(n, target))





