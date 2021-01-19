"""
https://www.codewars.com/kata/520b9d2ad5c005041100000f/solutions/java
https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/java
https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

"""
import re
from Tester import verdict, log

# public static String java_version_of_pig_it(String original) {
#        return original.replaceAll("(\\w)(\\w*)", "$2$1ay");
# }

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

# def pig_it_mine(original):
#     words = list(original.split(" ")) 
#     x = " ".join(map(pigify, words))
#     return x 

# def pigify(word):
#     latin = ""
#     punctuation = ""  # maybe a . Maybe a !! Maybe a  !?
#     result = ""
#     for i in range(len(word)):
#         c = word[i]

#         if i == 0:
#             if c.isalnum():
#                 latin = c + "ay"
#             else:
#                 punctuation = c
#         else:
#             if c.isalnum():
#                 result += c
#             else:
#                 punctuation += c 
#     r = result + latin + punctuation
#     print(r)
#     return r

if __name__ == '__main__':

        verdict(pig_it("Hello world !"),"elloHay orldway !")
        verdict(pig_it("Pig latin is cool"), "igPay atinlay siay oolcay")
        verdict(pig_it("Pig latin."), "igPay atinlay.")
        verdict(pig_it("yz !"), "zyay !")
        verdict(pig_it("yz!"), "zyay!")


