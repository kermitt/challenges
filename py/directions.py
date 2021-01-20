"""
https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
"""
from Tester import verdict, log

opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        r = "_"
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
            r = "P"
        else:
            new_plan.append(d)
        
    return new_plan


def dirReduc_mine(arr):
    separator = ''
    str = separator.join(arr)

    str = str.replace("NORTH", "N")
    str = str.replace("SOUTH", "S")
    str = str.replace("EAST", "E")
    str = str.replace("WEST", "W")

    dyads = ["NS", "EW", "SN", "WE" ]
    keepAlive = True
    before = 10000; 
    while keepAlive == True:
        for d in dyads:
            str = str.replace(d, "")
        if len(str) < before:
            before = len(str)
        else:
            keepAlive = False
    result = list(str)
    for i in range(len(result)):
        if result[i] == "W": result[i] = "WEST"
        if result[i] == "E": result[i] = "EAST"
        if result[i] == "N": result[i] = "NORTH"
        if result[i] == "S": result[i] = "SOUTH"

    return result


if __name__ == '__main__':
        verdict(['WEST'], dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
        #verdict(["NORTH", "WEST", "SOUTH", "EAST"], dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))
        verdict(["EAST", "NORTH"],dirReduc(["EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST"]))


