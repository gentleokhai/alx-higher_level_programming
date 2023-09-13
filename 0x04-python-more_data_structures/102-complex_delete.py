#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Create a list to store keys to be deleted
    keys_to_delete = []

    # Iterate through the dictionary and find keys with the specified value
    for key, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(key)

    # Delete the keys found in the previous step
    for key in keys_to_delete:
        del a_dictionary[key]

