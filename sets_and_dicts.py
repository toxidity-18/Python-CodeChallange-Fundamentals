
def merge_dicts(dict1, dict2):
    """Merges two dictionaries."""
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        merged_dict[key] = merged_dict.get(key, 0) + value
    return merged_dict

#  usage:

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}

merged_dict = merge_dicts(dict1, dict2)

print("Merged dictionary:")
for key, value in merged_dict.items():
    print(f"{key}: {value}")