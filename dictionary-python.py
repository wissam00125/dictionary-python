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
    
    
print(merge_dictionaries({"a": 1, "b": 2, "c": 3, "k": 5},  {"k": 80, "b": 10, "d": 4}))  # if two dict are not empty
print(merge_dictionaries({"x": 400, "y": 300}, {})) # if dict2  is empty
print(merge_dictionaries({}, {"x": 15, "y": 25, "z": 12})) # if dict1 is empty
print(merge_dictionaries({},  {})) # if both dict are empty


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

company_employees = {
    "Engineering": {
        "Alice": {"age": 30, "role": "Software Engineer"},
        "Bob": {"age": 28, "role": "DevOps Engineer"}
    },
    "HR": {
        "Charlie": {"age": 35, "role": "HR Manager"}
    },
    "IT": { 
       "Ahmad": {"age": 25, "role": "Software Engineer"},
       "Ali": {"age": 32, "role": "System Administrator"},
    },
    
}

# print the company employees
for department, employees in company_employees.items():
    print(f"\nDepartment: {department}")
    for name, details in employees.items():
        print(f"   Name: {name}, Age: {details['age']}, Role: {details['role']}")


        
# Add new employee
def add_employee(department, name, age, role):
    if department in company_employees:
        company_employees[department][name] = {"age": age, "role": role}
    else:
        print(f"Department '{department}' does not exist.")


add_employee("Engineering", "David", 27, "Data Scientist")

# Count the total number of employees in the company
def count_total_employee(dictionary):
    total_number_employee = 0
    if not dictionary:
        return 0
    for department in dictionary:
        total_number_employee += len(dictionary[department])
        
    return total_number_employee

print(f"The total number of employees in the company: {count_total_employee(company_employees)}")


dictionary1 = {"Alice": 10, "Bob": 20, "Charlie": 10, "David": 30}
# {10: ["Alice", "Charlie"], 20: ["Bob"], 30: ["David"]}
dictionary2 = {}

def group_by_value(dictionary):
    if not dictionary:
        print('The dictionary is empty!')
        exit()
        
    new_dictionary = dict()
    for key, value in dictionary.items():
        if value in new_dictionary:
            new_dictionary[value].append(key)
        else:
            new_dictionary[value] = [key]
    return new_dictionary

print(group_by_value(dictionary1))
print(group_by_value(dictionary2))



