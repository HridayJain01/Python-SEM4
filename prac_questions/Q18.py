result = []

for num in range(100, 401):
    num_str = str(num)
    all_even = True
    for digit in num_str:
        if int(digit) % 2 != 0:
            all_even = False
            break
    if all_even:
        result.append(num)

comma_separated = ""
for i in range(len(result)):
    comma_separated += str(result[i])
    if i != len(result) - 1:
        comma_separated += ","

print(comma_separated)


