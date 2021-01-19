const {log, verdict} = require('./Tester')

//https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/javascript
// def pig_it(text):
//     lst = text.split()
//     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

function pig_it(str) {
 //Code here
 return str.replace(/\b(\w)(\w*)\b/g,"$2$1ay");

}
const pig_it_other = (original ) => {
    let words = original.split(" ") 
    words = words.map(word => pigify_regex(word)).join(" ")
    return words
//    return original.replace(/(\\w)(\\w*)/g, /$2$1ay/);
}
const pigify_regex = (word) => {
    return word.replace(/(\w)(\w*)(\s|$)/g, "\$2\$1ay\$3")
    
//    return word.replace(/(\w)(\w*)(\s|$)/g, "\$2\$1ay\$3")
}
const pig_it_mine = (original) => {
    let words = original.split(" ") 
    words = words.map(word => pigify(word)).join(" ")
    return words
}
const pigify = ( word ) => { 
    if ( isAlphaNumeric(word)) {

        return word.substring(1, word.length) + word.charAt(0) + "ay"
    } else {
        // it is a ! or something - It isn't a word
        // return "sfkg"

        return word 
    }
}
const isAlphaNumeric = ( word ) => { 
    if (word.match(/^[0-9a-zA-Z]+$/)) {
        return true
    } else {
        return false
    }
}

verdict(pig_it("Hello world !"),"elloHay orldway !")
// verdict(pig_it("Pig latin is cool"), "igPay atinlay siay oolcay")
// verdict(pig_it("Pig latin ."), "igPay atinlay.")
verdict(pig_it("yz!"), "zyay!")
verdict(pig_it("yz !"), "zyay !")


