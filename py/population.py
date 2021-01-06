"""
In a small town the population is p0 = 1000 at the beginning of a year. 
The population regularly increases by 2 percent per year and moreover 
50 new inhabitants per year come to live in the town. 
How many years does the town need to see its population greater or equal 
to p = 1200 inhabitants?

At the end of the first year there will be: 
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

At the end of the 2nd year there will be: 
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (number of inhabitants is an integer)

At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213

It will need 3 entire years.

https://www.codewars.com/kata/563b662a59afc2b5120000c6/train/python

"""
def nb_year(p0, percent, aug, p):
    #p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)
    percent *= 0.01
    loop = 0 
    while p0 < p and loop < 100000:
        p0 += p0 * percent
        p0 += aug    
        # print("loop {} has {} and {}  ".format( loop, p0, percent ))
        loop += 1
    return loop    



def log( actual, expected):
    r = "FAIL"
    if actual == expected:
        r = "PASS"
    print("{}  {}  {} ".format(r, actual, expected))

log(nb_year(1000, 2, 50, 1200), 3)
log(nb_year(1500, 5, 100, 5000), 15)
log(nb_year(1500000, 2.5, 10000, 2000000), 10)
log(nb_year(1500000, 0.25, 1000, 2000000), 94)