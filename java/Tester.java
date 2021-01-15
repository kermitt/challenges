public class Tester {
	static void log(String s) { 
		System.out.println(s);
	}
	static void verdict(String actual, String expected) {
		String didPass = "FAIL";
		if ( actual.equals(expected)) {
			 didPass = "PASS";
		}
		String s = String.format("%s |%s|   ---> |%s|", didPass, actual, expected);
		System.out.println(s);
	}
//	public static void main(String...strings) {
//		Tester t = new Tester();
//		t.verdict("ONE",  "ONE");
//		t.verdict("ONE",  "TWO");
//	}
}
