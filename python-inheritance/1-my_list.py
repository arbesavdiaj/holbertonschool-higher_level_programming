#!/usr/bin/python3
'''
comment
'''


class MyList(list):
    '''A class that inherits from list'''
    def print_sorted(self):
        '''prints a sorted list'''
        print(sorted(self))
