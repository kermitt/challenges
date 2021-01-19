const {log, verdict} = require('./Tester')

//https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/javascript
function pig_it(original) {
    return original.replace(/\b(\w)(\w*)\b/g,"$2$1ay");
}

verdict(pig_it("Hello world !"),"elloHay orldway !")
verdict(pig_it("Pig latin is cool"), "igPay atinlay siay oolcay")
verdict(pig_it("Pig latin ."), "igPay atinlay .")
verdict(pig_it("yz!"), "zyay!")
verdict(pig_it("yz !"), "zyay !")
verdict(pig_it("o"), "oay")
verdict(pig_it("."), ".")


