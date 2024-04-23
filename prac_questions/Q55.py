add_15 = lambda x: x + 15
number = 10
result = add_15(number)
print("Result after adding 15 to", number, ":", result)


add_15 = lambda x: x + 15

number = [1, 2, 3, 4, 5]
result = list(map(add_15, number))
print("Result after adding 15 to each element of", number, ":", result)

