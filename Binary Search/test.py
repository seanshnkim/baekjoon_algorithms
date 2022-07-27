# HOW TO change dictionary into list
# Sehyun Kim, 2022.07.23(July 23rd, 2022)

dict1 = {'red': 32, 'green':21, 'blue': 43}
dict2 = {'name': 'Ravi', 'age': 23, 'marks': 56}

print(type(dict1.items()))

# 'dict_items' object has no attribute 'sort'
# sortedList = dict1.items().sort()
# type(dict2list) = <class 'list'>
dict2list = list(dict1.items())
# 'dict_items' object has no attribute 'sort'
dict2list.sort()

# swap keys and values in a dictionary
dict1_swapped = {value:key for key, value in dict1.items()}
dict2list2 = list(dict1_swapped.items())
# Python list of tuples is sorted by the first item of each tuple
dict2list2.sort()

print(dict2list)
print(dict2list2)
