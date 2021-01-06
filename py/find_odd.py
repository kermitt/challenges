"""
https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
"""
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

def MINE_find_it(seq):
    seen = {}
    for n in seq:
        if n in seen:
            seen[n] += 1
        else:
            seen[n] = 1

    the_odd_number = -1
    for k in seen:
        v = seen[k]
        if v % 2 == 1:
            the_odd_number = k
            #print("YAY %i   %i".format( k, v))
        #else:
            #print("BOO %i   %i".format( k, v))

    return the_odd_number


def log(actual, expect): 
    if actual == expect:
        print("PASS {} --------------> {} ".format(actual, expect))
    else :
        print("FAIL {} --------------> {} ".format(actual, expect))

log(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
log(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1)
log(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5)
log(find_it([10]), 10)
log(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10)
log(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1)