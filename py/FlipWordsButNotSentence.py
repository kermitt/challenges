"""
Reverse words in a sentence w/o messing w/ the spaces
given: abc  xyz    opq
yield: cba  zyx    qpo
"""
from Tester import verdict, log

def solution(original):
    words = list(original.split(" ")) 
    x = " ".join(map(flipword, words))
    return x 

def flipword(word): 
    # 'generator expression' TODO: Look up
    return ' '.join(''.join(reversed(letter)) for letter in word.split())

if __name__ == '__main__':
    verdict(solution("abc  xyz    opq"), "cba  zyx    qpo")
    verdict(solution("   "), "   ")
    verdict(solution("This_is_a_long_string"), "gnirts_gnol_a_si_sihT")
    verdict(solution(""), "")
