def log(s): 
    print("|{}|".format(s))

def verdict(actual, expected):
    didPass = "FAIL"
    if actual == expected:
        didPass = "PASS"
	    
    print("{} |{}|   ---> |{}|".format(didPass, actual, expected))

