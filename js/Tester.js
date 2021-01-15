function log(s) { 
    console.log(`|${s}|`)
}

function verdict(actual, expected) {
    let isFine = "FAIL"
    if ( actual === expected ) { 
        isFine = "PASS"
    } 
    console.log(`${isFine} |${actual}|  ----> |${expected}|`)
}
module.exports = {log, verdict}