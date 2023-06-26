#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ints_print = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ints_print += 1
        except(TypeError, ValueError):
            pass
    print("")
    return (ints_print)
