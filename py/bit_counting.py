"""
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

https://www.codewars.com/kata/526571aae218b8ee490006f4/python
"""

def count_bits(n):
    # Python's string format method can take a format spec. 
    s = "{0:b}".format(n)
    count = 0 
    for char in s:
        if char == "1":
            count += 1 

    return count 
    
def log(actual, expected):
    if actual == expected:
        print("PASS {} ----------> {} ".format( actual, expected ))
    else:
        print("PASS {} ----------> {} ".format( actual, expected ))

log(count_bits(0), 0)
log(count_bits(4), 1)
log(count_bits(7), 3)
log(count_bits(9), 2)
log(count_bits(10), 2)
