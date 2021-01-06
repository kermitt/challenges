
// https://www.codewars.com/kata/578553c3a1b8d5c40300037c/javascript
// Given an array of ones and zeroes, convert the equivalent binary value to an integer.

const binary_array_to_number = (arr) => {
    let s = ""
    arr.forEach((item)=>{
        s += item
    })
    n = parseInt(s,2)
    return n 
}
const log = (actual, expect) => { 
    if (actual == expect) {
        console.log(`PASS ${actual} --------------> ${expect} `)
    }
    else {
        console.log(`FAIL ${actual} --------------> ${expect} `)
    }
}

log(binary_array_to_number([0,0,0,0]), 0)
log(binary_array_to_number([0,0,0,1]), 1)
log(binary_array_to_number([0,0,1,0]), 2)
log(binary_array_to_number([0,0,1,1]), 3)
log(binary_array_to_number([0,1,0,0]), 4)
log(binary_array_to_number([0,1,0,1]), 5)
log(binary_array_to_number([0,1,1,0]), 6)
log(binary_array_to_number([0,1,1,1]), 7)
log(binary_array_to_number([1,0,0,0]), 8)
log(binary_array_to_number([1,0,0,1]), 9)
log(binary_array_to_number([1,0,1,0]), 10)
log(binary_array_to_number([1,0,1,1]), 11)
log(binary_array_to_number([1,1,0,0]), 12)
log(binary_array_to_number([1,1,0,1]), 13)
log(binary_array_to_number([1,1,1,0]), 14)
log(binary_array_to_number([1,1,1,1]), 15)