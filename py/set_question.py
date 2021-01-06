
"""
https://www.codewars.com/kata/5fddfbe6a65636001cc4fcd2/train/python

set! is a card game where you compete with other players, to find out who can find a set of cards first.
Your task is to write a function that checks if a collection of three input cards qualifies as a set.

"""

def is_extreme(ary):
    # True = everything is unique OR everything is the same.
    s = set()
    for x in ary:
        s.add(str(x))
    
    n1 = len(ary)
    n2 = len(s)
    if n2 == 1:
        # same!
        return True 
    elif n1 == n2:
        # unique
        return True 
    else:
        return False



def is_valid_set(quantities, shapes, colours, patterns):
    bools = [] 
    bools.append(is_extreme(quantities))
    bools.append(is_extreme(shapes))
    bools.append(is_extreme(colours))
    bools.append(is_extreme(patterns))
    # m = list(zip(shapes, colours, patterns))
    # bools.append(is_extreme(m[0]))
    # bools.append(is_extreme(m[1]))
    # bools.append(is_extreme(m[2]))
    for b in bools:
        if b == True:
            return True
    return False


def log(expect, name, actual ):
    if expect == actual:
        print("PASS {} ".format(name))
    else:
        print("FAIL {} got {} ".format( name, actual ))

log(True, "test_all_different....", is_valid_set([1,2,3], ['A','B','C'], ['R','S','T'], ['Z','Y','X']))
log(True, "same_different........", is_valid_set([1,1,1], ['C','A','B'], ['T','T','T'], ['Y','Z','X']))
log(True, "same..................", is_valid_set([3,1,2], ['A','C','B'], ['S','R','T'], ['X','X','X']))
log(False, "invalid everything...", is_valid_set([1,2,1], ['A','A','B'], ['S','T','T'], ['Z','Z','Y']))
# I do not grok the last one
#log(False, "invalid quantities...", is_valid_set([1,1,3], ['A','B','C'], ['R','S','T'], ['Z','Y','X']))
log(False, "invalidate quantities", is_valid_set([1,1,3], ['diamond','snake','capsule'], ['green','blue','red'], ['blank','striped','solid']))
