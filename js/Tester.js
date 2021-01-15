function log(s) { 
    console.log(`|${s}|`)
}

function verdict(actual, expected) {
    let isFine = "FAIL"
    if ( actual == expected ) { 
        isFine = "PASS"
    } 
    console.log(`${isFine} |${actual}|  ----> |${expected}|`)
}

const divmod = (numerator, denominator) => {
    /*
    Floor Division
    quotient = n // d 
    remainder = n % d
    */
    return {
        quotient:Math.floor(numerator/denominator),
        remainder:numerator % denominator
    }
}

module.exports = {log, verdict}


//https://github.com/kermitt/challenges/blob/main/py/FlipWordsButNotSentence.py
//https://github.com/kermitt/challenges/blob/main/java/FlipWordsButNotSentence.java