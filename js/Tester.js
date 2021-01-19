function log(s) { 
    console.log(`|${s}|`)
}

function verdict2(actual, expected) {
    const a = JSON.stringify( actual )
    const b = JSON.stringify(expected)
    let isFine = "FAIL"
    if ( a == b ) { 
        isFine = "PASS"
    } 
    console.log(`${isFine} |${actual}|  ----> |${expected}|`)
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
const isAlphaNumeric = ( word ) => { 
    if (word.match(/^[0-9a-zA-Z]+$/)) {
        return true
    } else {
        return false
    }
}
module.exports = {log, verdict, isAlphaNumeric, divmod, verdict2}


//https://github.com/kermitt/challenges/blob/main/py/FlipWordsButNotSentence.py
//https://github.com/kermitt/challenges/blob/main/java/FlipWordsButNotSentence.java