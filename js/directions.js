// https://www.codewars.com/kata/550f22f4d758534c1100025a/train/javascript
const {log, verdict2} = require('./Tester')

const opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

function dirReduc(plan) { 
    new_plan = []
    plan.forEach((d) => {
        let r = "_"
        if ( new_plan.length > 0 && new_plan[-1] == opposite[d] ) {
            new_plan.pop()
        } else {
            new_plan.push(d)
        }
    })        
    return new_plan
}


function dirReduc_js(arr) {
    let str = arr.join(''); 
    let pattern = /NORTHSOUTH|EASTWEST|SOUTHNORTH|WESTEAST/;
    while (pattern.test(str)) { 
        str = str.replace(pattern,'');
    }
    // console.log("BEFORE: " +  typeof str )
    let after =  str.match(/(NORTH|SOUTH|EAST|WEST)/g)||[];
    // console.log("AFTER  " + typeof after )
    return after 
  }



function dirReduc_mine(directions) {
    let x = directions.join(" ")
    const dyads = [
        "NORTH SOUTH",
        "SOUTH NORTH",
        "EAST WEST",
        "WEST EAST"
    ] 

    let  before = 10000
    let keepAlive = true 
    let loop = 0
    while ( keepAlive == true ) {
        loop++
        dyads.forEach((item) => { 
            x = zap(x, item)
        }) 
        if ( x.length < before ) {
            before = x.length
            keepAlive = true
            // console.log( loop, before, x.length , x )
        } else {
            keepAlive = false 
        }
    }
    // console.log(x)
    // return x
    if ( x.length < 1 ) {
        return []
    } else {
    return x.split(" ")
    }
}
function zap(x, kill) {
    let re = new RegExp(kill,"g");
    x = x.replace(re, "")
    x = x.replace(/  /g, ' ')
    return x.trim()

}



// dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])

verdict2(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ["WEST"])
verdict2(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]), ["NORTH", "WEST", "SOUTH", "EAST"])
verdict2(dirReduc(["NORTH", "SOUTH", "EAST", "WEST", "EAST", "WEST"]), [])


