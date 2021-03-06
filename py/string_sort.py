"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

https://www.codewars.com/kata/55c45be3b2079eccff00010f/python
"""

def order(sentence):
    ary = sentence.split(" ")
    accum = ""
    for i in range(1, 10):
        for word in ary:
            if str(i) in word:
                accum += word
                accum += " "
    accum = accum.strip()
    return accum

def log( expect, actual):
    if ( expect == actual ):
        print("PASS |{}| ------------e-> |{}|".format( actual, expect ))
    else:
        print("FAIL |{}| ------------e-> |{}| ".format(actual, expect ))

log(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
log(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
log(order(""), "")
