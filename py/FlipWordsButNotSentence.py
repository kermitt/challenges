"""
Reverse words in a sentence w/o messing w/ the spaces
given: abc  xyz    opq
yield: cba  zyx    qpo
"""
from Tester import verdict, log

def flip(original):
    # I wonder how to do this in python 

    word = [char for char in original]
    begin = 0
    end = len(word) - 1
    while begin < end:
        temp = word[begin]
        word[begin] = word[end]
        word[end] = temp
        begin += 1
        end -= 1

    r = "".join(word)
    return r 

def solution(original):
    words = list(original.split(" ")) 
    x = " ".join(map(flip, words))
    return x

if __name__ == '__main__':
    verdict(solution("abc  xyz    opq"), "cba  zyx    qpo")
    verdict(solution("   "), "   ")
    verdict(solution("This_is_a_long_string"), "gnirts_gnol_a_si_sihT")
