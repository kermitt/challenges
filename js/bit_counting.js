
// https://www.codewars.com/kata/578553c3a1b8d5c40300037c/javascript
// https://www.codewars.com/kata/526571aae218b8ee490006f4/javascript
// Given an array of ones and zeroes, convert the equivalent binary value to an integer.

const count_bits = n => n.toString(2)
                        .split('')
                        .filter(ele => ele == 1)
                        .length


const MINE_countBits = (n) => {
    let count = 0
    const s = (n >>> 0).toString(2)
    arr = s.split("")
    arr.forEach((char)=>{
        if ( char == "1") {
            count++
        }
    })
    return count
}

const log = (actual, expect) => { 
    if (actual == expect) {
        console.log(`PASS ${actual} --------------> ${expect} `)
    }
    else {
        console.log(`FAIL ${actual} --------------> ${expect} `)
    }
}

log(count_bits(0), 0)
log(count_bits(4), 1)
log(count_bits(7), 3)
log(count_bits(9), 2)
log(count_bits(10), 2)
