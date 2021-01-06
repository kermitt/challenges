"""
Write a function that accepts an array of 10 integers (between 0 and 9), 
that returns a string of those numbers in the form of a phone number.

https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
"""
def create_phone_number(n):
    return "(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n)

def MINE_create_phone_number(n):
    accum = "("
    step = 0
    for num in n:
        accum += str(num)
        step += 1 
        if step == 3:
            accum += ") "
        elif step == 6:
            accum += "-"        
    return accum



def log(actual, expected):
    if actual == expected:
        print("PASS {}    {} ".format(actual, expected ))
    else:
        print("FAIL {}   {} ".format(actual, expected ))

log(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
log(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
log(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
log(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
log(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")