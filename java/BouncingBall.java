/*
// https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/java
// A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.
// He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
// His mother looks out of a window 1.5 meters from the ground.
// How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?
// Three conditions must be met for a valid experiment:
//     Float parameter "h" in meters must be greater than 0
//     Float parameter "bounce" must be greater than 0 and less than 1
//     Float parameter "window" must be less than h.
// If all three conditions above are fulfilled, return a positive integer, otherwise return -1.
*/

public class BouncingBall {

    public static int bouncingBall (double h, double bounce, double window) {
        if ( h < 0 || ( bounce <= 0 || bounce >= 1 ) || window > h ) {
            return -1; 
        }
        int loop = -1; 
        while ( h > window && loop < 100 ) {
            //console.log( loop, h, bounce, window)
            h *= bounce;  
            loop += 2;
        }
        return loop; 
    } 

    private static void test(int expected, int actual) {
        if ( expected == actual ) {
            System.out.println("PASS " + expected + "   " + actual ); 
        } else {
            System.out.println("FAIL " + expected + "   " + actual ); 
        }
    }
    public static void main(String[] args) {
        test(3, bouncingBall(3.0, 0.66, 1.5));
        test(15, bouncingBall(30.0, 0.66, 1.5));
	}
}
