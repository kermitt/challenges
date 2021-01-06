"""
Create a function that returns the sum of the two lowest positive numbers 
given an array of minimum 4 positive integers. 
No floats or non-positive integers will be passed.
https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
"""

def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    return numbers[0] + numbers[1]


def log(expected, actual):
    if expected == actual:
        print("PASS {}    {} ".format( expected, actual )) 
    else:
        print("FAIL {}    {} ".format( expected, actual )) 


log(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
log(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
log(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)