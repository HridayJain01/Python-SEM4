#Sort a given dictioary by key

unsorted_dict = {
    "banana": 5,
    "apple": 2,
    "orange": 10,
    "grape": 7,
    "kiwi": 3
}

sorted_keys = sorted(unsorted_dict.keys())

sorted_dict = {key: unsorted_dict[key] for key in sorted_keys}

print("Unsorted dictionary:", unsorted_dict)
print("Sorted dictionary by key:", sorted_dict)