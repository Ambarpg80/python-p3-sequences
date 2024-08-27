#!/usr/bin/env python3

def print_fibonacci(length):
    my_list = []
    i = 0
    if length == 0:
        print(my_list)   
    elif length == 1:
        my_list.append(0)
        print(my_list)
    elif length >= 2:
        my_list.append(0)
        my_list.append(1) 
        while len(my_list) < length:
            my_list.append(my_list[-1] + my_list[-2])
            i+=1       
        print(my_list)  