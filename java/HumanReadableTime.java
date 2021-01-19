package java;

import java.util.stream.Collectors;
import java.util.stream.Stream;

public class HumanReadableTime extends Tester {

	public static void main(String... strings) {
		verdict(solution("abc  xyz    opq"), "cba  zyx    qpo");
		verdict(solution("   "), "   ");
		verdict(solution("This_is_a_long_string"), "gnirts_gnol_a_si_sihT");
		verdict(solution(""), "");
	}
}
