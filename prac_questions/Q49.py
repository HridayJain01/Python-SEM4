# remove duplicates from the dictionary

def remove_duplicates(dictionary):
    seen_values = set()
    unique_dict = {}

    for key, value in dictionary.items():
        if value not in seen_values:
            seen_values.add(value)
            unique_dict[key] = value

    return unique_dict

example_dict = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 2,
    "e": 2
}

result_dict = remove_duplicates(example_dict)

print("Original dictionary:", example_dict)
print("Dictionary without duplicates:", result_dict)