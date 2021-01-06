
// https://www.codewars.com/kata/54da5a58ea159efa38000836/train/javascript
// Given an array of integers, find the one that appears an odd number of times.

// There will always be only one integer that appears an odd number of times.
function findOdd(A) {
    var obj = {};
    A.forEach(function(el){
      obj[el] ? obj[el]++ : obj[el] = 1;
    });
    
    for(prop in obj) {
      if(obj[prop] % 2 !== 0) return Number(prop);
    }
  }

function MINE_findOdd(A) {
    let seen = {};
    A.forEach((n)=>{
        if ( seen.hasOwnProperty(n)) {
            seen[n]++
        } else {
            seen[n] = 1
        }
    })
    the_odd_number = -1

    for ( let k in seen ) {
        let v = seen[k]
        if ( v % 2 == 1 ) {
            the_odd_number = k
            // console.log("YAY " + k + "  " + v )
        } else {
            // console.log("BOO " + k + "  " + v )
        }
    }
    return parseInt(the_odd_number)
  }


const log = (actual, expect) => { 
    if (actual == expect) {
        console.log(`PASS ${actual} --------------> ${expect} `)
    }
    else {
        console.log(`FAIL ${actual} --------------> ${expect} `)
    }
}

log(findOdd([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5);
log(findOdd([1,1,2,-2,5,2,4,4,-1,-2,5]), -1);
log(findOdd([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
log(findOdd([10]), 10);
log(findOdd([1,1,1,1,1,1,10,1,1,1,1]), 10);
log(findOdd([5,4,3,2,1,5,4,3,2,10,10]), 1);