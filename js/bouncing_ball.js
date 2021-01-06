// https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/javascript
// A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.
// He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
// His mother looks out of a window 1.5 meters from the ground.
// How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?
// Three conditions must be met for a valid experiment:
//     Float parameter "h" in meters must be greater than 0
//     Float parameter "bounce" must be greater than 0 and less than 1
//     Float parameter "window" must be less than h.
// If all three conditions above are fulfilled, return a positive integer, otherwise return -1.



const bouncing_ball = (h, bounce, window) => {
    if ( h < 0 || ( bounce <= 0 || bounce >= 1 ) || window > h ) {
        return -1 
    }
    loop = -1
    while ( h > window && loop < 100 ) {
        //console.log( loop, h, bounce, window)
        h *= bounce 
        loop += 2 
    }

    return loop 
} 


const testing = (h, bounce, window, expected) => {
    actual = bouncing_ball(h, bounce, window)
    if ( actual == expected) {
        console.log(`PASS ${actual}   ${expected}`)
    } else {
        console.log(`FAIL ${actual}   ${expected}`)
    }
}        
function tests() {
    testing(2, 0.5, 1, 1)
    testing(3, 0.66, 1.5, 3)
    testing(30, 0.66, 1.5, 15)
    testing(30, 0.75, 1.5, 21)
}
tests()