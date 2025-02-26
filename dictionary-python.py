# functions and dictionaries

# merging two dictionaries
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
    
    
# print(merge_dictionaries({"a": 1, "b": 2, "c": 3, "k": 5},  {"k": 80, "b": 10, "d": 4}))  # if two dict are not empty
# print(merge_dictionaries({"x": 400, "y": 300}, {})) # if dict2  is empty
# print(merge_dictionaries({}, {"x": 15, "y": 25, "z": 12})) # if dict1 is empty
# print(merge_dictionaries({},  {})) # if both dict are empty


# count word frequency in a sentence
def count_word_frequency(sentence):
    result = dict()
    if not sentence:
        return {}
    for word in sentence.strip().split():
        word = word.lower()
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


sentence1 = "apple orange banana apple orange apple banana"
sentence2 = "Ahmad Samer Wissam Khalid AHMAD Fadi wissam Samer"

print(count_word_frequency(sentence1))
print(count_word_frequency(sentence2))

