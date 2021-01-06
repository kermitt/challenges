"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 
below the number passed in.

    Note: If the number is a multiple of both 3 and 5, only count it once. 
    Also, if a number is negative, return 0(for languages that do have them)

https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
"""

def solution(number):
    sum = 0 
    for n in range(number):
        if n > 0:
            if n % 3 == 0 and n % 5 == 0:
                sum += n
            elif n % 3 == 0:
                sum += n
            elif n % 5 == 0:
                sum += n
    return sum


def log(actual, expected):
    if actual == expected:
        print("PASS {}    {}".format(actual, expected )) #
    else:
        print("FAIL {}    {}".format(actual, expected )) #


log(solution(10), 23)