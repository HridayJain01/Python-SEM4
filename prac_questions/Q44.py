#Remove a key from a dictionary

sample_dict = {
    "name": "Kandi",
    "age": 23,
    "city": "Malibu",
    "profession": "Engineer"
}

print("Original dictionary:", sample_dict)

del sample_dict["age"] 
print("After removing age: ", sample_dict)

removed_value = sample_dict.pop("city")
print("After removing city:", sample_dict)
print("Value returned by pop:", removed_value)