const {log, verdict} = require('./Tester')
const flip = (word) => {
    // huh - looks like java
    return word
        .split("")
        .reverse()
        .join("");
}
const solution = (original) => { 
    let words = original.split(" ") 
    words = words.map(word => flip(word)).join(" ")
    return words

}
verdict(solution("abc  xyz    opq"), "cba  zyx    qpo")
verdict(solution("   "), "   ")
verdict(solution("This_is_a_long_string"), "gnirts_gnol_a_si_sihT")
verdict(solution(""), "")