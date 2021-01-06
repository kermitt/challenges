"""
Given an array of ones and zeroes, convert the equivalent binary value to an integer.

https://www.codewars.com/kata/578553c3a1b8d5c40300037c/python

"""
def binary_array_to_number(arr):
    # https://dev.to/aspittel/comment/6gp1
    # WHat does , 2) mean?
    return int(''.join(str(i) for i in arr), 2)

def log( actual, expect): 
    if actual == expect:
        print("PASS {} --------------> {} ".format(actual, expect ))
    else:
        print("FAIL {} --------------> {} ".format(actual, expect ))


log(binary_array_to_number([0,0,0,0]), 0)
log(binary_array_to_number([0,0,0,1]), 1)
log(binary_array_to_number([0,0,1,0]), 2)
log(binary_array_to_number([0,0,1,1]), 3)
log(binary_array_to_number([0,1,0,0]), 4)
log(binary_array_to_number([0,1,0,1]), 5)
log(binary_array_to_number([0,1,1,0]), 6)
log(binary_array_to_number([0,1,1,1]), 7)
log(binary_array_to_number([1,0,0,0]), 8)
log(binary_array_to_number([1,0,0,1]), 9)
log(binary_array_to_number([1,0,1,0]), 10)
log(binary_array_to_number([1,0,1,1]), 11)
log(binary_array_to_number([1,1,0,0]), 12)
log(binary_array_to_number([1,1,0,1]), 13)
log(binary_array_to_number([1,1,1,0]), 14)
log(binary_array_to_number([1,1,1,1]), 15)

