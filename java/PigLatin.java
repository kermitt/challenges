//https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/java
/*
pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !
*/

import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.Arrays;
import java.util.stream.Collectors;

public class PigLatin extends Tester {

    private static String logic(String original ) {
        char[] charArray = original.toCharArray();
        int i = 0; 
        String latin = ""; 
        String punctuation = "";
        String result = ""; 
        for(char c:charArray) {
            if ( i == 0 ) {
                if (Character.isLetterOrDigit(c)) {
                    latin = String.valueOf(c) + "ay";
                } else {
                    punctuation  += String.valueOf(c);
                }
            } else {
                if (Character.isLetterOrDigit(c)) {
                    result += String.valueOf(c); 
                } else {
                    punctuation  += String.valueOf(c);
                }
            }
            i++;
        }
        return result + latin + punctuation;
    }

	public static String pigIt_mine(String original) {
        String space = " "; 
        return Stream
            .of(original.split(space))
            .map(word -> logic(word))
            .collect(Collectors.joining(space));

	}
    public static String pigIt(String original) {
        return original.replaceAll("(\\w)(\\w*)", "$2$1ay");

    }

    public static String pigIt_second(String str) {
        return Arrays.stream(str.split(" ")).map(PigLatin::pigify).collect(Collectors.joining(" "));
    }

    private static String pigify(String word){
        return word.length() > 1 || Character.isLetter(word.charAt(0)) ? word.substring(1) + word.charAt(0) + "ay" : word;
               
    }

	public static void main(String... strings) {
        verdict(pigIt("Hello world !"),"elloHay orldway !");
        verdict(pigIt("Pig latin is cool"), "igPay atinlay siay oolcay");
        verdict(pigIt("Pig latin."), "igPay atinlay.");
        verdict(pigIt("z!"), "zay!");
        verdict(pigIt("z!"), "zay!");
        verdict(pigIt("yz!"), "zyay!");
        verdict(pigIt("yz !"), "zyay !");
        verdict(pigIt("o"), "oay");
        verdict(pigIt("."), ".");

	}
}


