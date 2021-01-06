

// https://www.codewars.com/kata/54da5a58ea159efa38000836/train/java


import java.util.*;

public class FindOdd {

    public static int findIt (int[] ary) {

        System.out.println("FINISH THIS https://www.codewars.com/kata/54da5a58ea159efa38000836/train/java"); 

        // Map<Integer, Integer> seen = new HashMap<>();
        // for (int i : ary) { 
        //     if ( seen.containsKey(i)) {
        //         seen.get(i)++:
        //     } else {
        //         seen.put(i, 1); 
        //     }


        // }
        return 5 ; 
    } 

    private static void test(int expected, int actual) {
        if ( expected == actual ) {
            System.out.println("PASS " + expected + "   " + actual ); 
        } else {
            System.out.println("FAIL " + expected + "   " + actual ); 
        }
    }
    public static void main(String[] args) {
        test(5, findIt(new int[]{20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5})); 
        test(-1, findIt(new int[]{1,1,2,-2,5,2,4,4,-1,-2,5})); 
        test(5, findIt(new int[]{20,1,1,2,2,3,3,5,5,4,20,4,5}));
        test(10, findIt(new int[]{10}));
        test(10, findIt(new int[]{1,1,1,1,1,1,10,1,1,1,1}));
        test(1, findIt(new int[]{5,4,3,2,1,5,4,3,2,10,10}));
    }
    


}
