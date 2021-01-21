//https://www.codewars.com/kata/52b7ed099cdc285c300001cd/python

const {log, verdict} = require('./Tester')

function isLeft(o, i) {
    let flag = false 
    const a = o[0]
    const b = o[1]
    const y = i[0]
    const z = i[1] 

    if ( a <= y && b >= y  ) {
        flag = true 
    }


    console.log( o , i, flag, "  |" , a, b, y, z )

}

function sumIntervals( LoL ) {
    let bounds = LoL[0]
    LoL.forEach((inner)=>{
        console.log(inner)
        addAnother = false
        let l1 = inner[0]
        let h1 = inner[1]
        bounds.forEach((bound)=>{


        })

    });
    return 6
} 

// verdict(sumIntervals([[1,5]]),4)
// verdict(sumIntervals([[1,5],[6,10]]),8)
// verdict(sumIntervals([[1,5],[1,5]]),4)
// verdict(sumIntervals([[1,4],[7, 10],[3, 5]]),7)

isLeft([10, 20], [0, 9])
isLeft([10, 20], [0, 10])
isLeft([10, 20], [0, 11])