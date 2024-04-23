# Map two lists into a dictionary 

keys = ["name", "age", "city"]
values = ["Kandi", 23, "Malibu"]

zipped_lists = zip(keys, values)

result_dict = dict(zipped_lists)

print("Mapped dictionary:", result_dict)