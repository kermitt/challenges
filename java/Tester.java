public class Tester {
	static void log(String s) { 
		System.out.println(s);
	}
	static void log(String[] ary) { 
		String a = "["; 
		for ( String aa : ary ) {
			a += aa + " ";
		}
		a = a.trim();
		a += "]";
		System.out.println(a);

	}

	static void verdict(String[] actual, String[] expected) {
		String didPass = "FAIL";
		String a = "["; 
		for ( String aa : actual ) {
			a += aa + " ";
		}
		a = a.trim();
		a += "]";
		String e = "["; 
		for ( String ee : expected ) {
			e += ee + " "; 
		}
		e = e.trim(); 
		e += "]";

		if ( a.equals(e) ) {
			didPass = "PASS";
	   }


		String s = String.format("%s %s  !!--> %s", didPass, a, e);
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
