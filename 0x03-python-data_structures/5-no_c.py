#!/usr/bin/python3

def no_c(my_string):
    my_list = list(my_string)
    for element in my_list:
        if element == 'c' or element == 'C':
            del(my_list[my_list.index(element)])
    return("".join(my_list))
