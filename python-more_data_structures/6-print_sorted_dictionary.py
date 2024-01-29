#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_items = [(k, a_dictionary[k]) for k in sorted(a_dictionary)]
    for item in sorted_items:
        print(f"{item[0]}: {item[1]}")
 