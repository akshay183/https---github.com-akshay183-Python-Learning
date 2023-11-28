# wife = {'name':"anushka",
#         'age':27}

# print(wife.pop())

# print(wife.__contains__('ag'))
# print('name' in wife)

# It’s possible to add an item to a dictionary in this way:

# >>> wife = {'name': 'Rose', 'age': 33}
# >>> if 'has_hair' not in wife:
# ...     wife['has_hair'] = True
# Using the setdefault method, we can make the same code more short:

# >>> wife = {'name': 'Rose', 'age': 33}
# >>> wife.setdefault('has_hair', True)
# >>> wife


# Merge two dictionaries
# For Python 3.5+:

# >>> dict_a = {'a': 1, 'b': 2}
# >>> dict_b = {'b': 3, 'c': 4}
# >>> dict_c = {**dict_a, **dict_b}
# Note that if there are common keys between dict_a and dict_b, the values 
# from dict_b will overwrite the values from dict_a for those keys in the resulting dict_c.
# >>> dict_c
# # {'a': 1, 'b': 3, 'c': 4}

# get()
# The get() method returns the value of an item with the given key. If the key doesn’t exist, it returns None:

# >>> wife = {'name': 'Rose', 'age': 33}
# You can also change the default None value to one of your choice:

# >>> wife = {'name': 'Rose', 'age': 33}

# >>> f'She is deeply in love with {wife.get("husband", "lover")}'
# # 'She is deeply in love with lover'


