import java.util.stream.Collectors;
import java.util.stream.Stream;

public class FlipWordsButNotSentence extends Tester {
	private static String space = " ";

	private static String flip(String s) {
        return new StringBuffer(s)
            .reverse()
            .toString();
	}

	private static String solution(String original) {

        if (original
            .trim()
            .isEmpty()) {
			return original;
		}
        return Stream
            .of(original.split(space))
            .map(word -> flip(word))
            .collect(Collectors.joining(space));
	}

	public static void main(String... strings) {
		verdict(solution("abc  xyz    opq"), "cba  zyx    qpo");
		verdict(solution("   "), "   ");
		verdict(solution("This_is_a_long_string"), "gnirts_gnol_a_si_sihT");
		verdict(solution(""), "");
	}
}
