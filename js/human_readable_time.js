const {log, verdict} = require('./Tester')

/*
https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59
*/

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
const pad = (num) =>{
    if ( num < 10 ) {
        return `0${num}`
    }
    return num
}
const make_readable = (seconds) => { 
    // hours, seconds = divmod(seconds, 60 ** 2)
    const hours_seconds = divmod(seconds, 60 * 60)
    const hours = pad(hours_seconds.quotient)
    seconds = hours_seconds.remainder

    const minutes_seconds = divmod(seconds, 60)
    const minutes = pad(minutes_seconds.quotient)
    seconds = pad(minutes_seconds.remainder)

    return `${hours}:${minutes}:${seconds}`
} 

verdict(make_readable(0), "00:00:00")
 verdict(make_readable(5), "00:00:05")
verdict(make_readable(60), "00:01:00")
verdict(make_readable(86399), "23:59:59")
verdict(make_readable(359999), "99:59:59")

