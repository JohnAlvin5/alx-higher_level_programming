#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    nmb_print = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            nmb_print += 1
        except IndexError:
            break
    print()
    return(nmb_print)
