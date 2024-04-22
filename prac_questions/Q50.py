#Check if a dictionary is mepty or not 

def is_dict_empty(dictionary):
    if len(dictionary) == 0:
        return True
    return False

empty_dict = {}
print("Is the dictionary empty?", is_dict_empty(empty_dict))

non_empty_dict = {"key": "value"}
print("Is the dictionary empty?", is_dict_empty(non_empty_dict))