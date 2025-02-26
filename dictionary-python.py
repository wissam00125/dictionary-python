# functions and dictionaries

def merge_dictionaries(dictionary1, dictionary2):
    # not dictionary: true if dict is empty
    # if both dictionaries are empty
    if not dictionary1 and not dictionary2:
        print("The two dictionaries are empty!")
        return {}
    if not dictionary2:
        return dictionary1
    dictionary1.update(dictionary2)
    return dictionary1
    
    
print(merge_dictionaries({"a": 1, "b": 2, "c": 3, "k": 5},  {"k": 80, "b": 10, "d": 4}))  # if two dict is not empty
print(merge_dictionaries({"x": 400, "y": 300}, {})) # if dict2  is empty
print(merge_dictionaries({}, {"x": 15, "y": 25, "z": 12})) # if dict 1 is empty
print(merge_dictionaries({},  {})) # if both dict are empty
