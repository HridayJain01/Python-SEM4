# Multiply all the items in a dictionary
import math

sample_dict = {
    "a": 2,
    "b": 3,
    "c": 4,
    "d": 5
}

product = math.prod(sample_dict.values())

print("Dictionary:", sample_dict)
print("Product of all values:", product)