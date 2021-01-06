"""
Spin words in a sentence of 5+ letters long.
""" 
def spin_words(sentence):
    words = sentence.split(" ")
    result = "" 
    for w in words:
        if len(w) >= 5:
            w = w[::-1]
        result += w 
        result += " "

    result = result.strip()
    return result 




def log( actual, expected):
    r = "FAIL"
    if actual == expected:
        r = "PASS"
    print("{}  {}  {} ".format(r, actual, expected))

log(spin_words("Welcome"), "emocleW")
log(spin_words("This is a test"), "This is a test")

log(spin_words("This is another test"), "This is rehtona test")
