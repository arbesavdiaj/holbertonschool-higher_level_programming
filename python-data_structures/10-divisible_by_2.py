#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result_list = []
    
    for el in my_list:
        if el / 2:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list