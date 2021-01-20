import java.util.ArrayList; 

public class Directions extends Tester {

    public static String[] dirReduc(String[] arr) {
        ArrayList<String> array = new ArrayList();
        array.add("NORTHSOUTH");
        array.add("SOUTHNORTH");
        array.add("EASTWEST");
        array.add("WESTEAST");
        ArrayList<String> result = new ArrayList();
        for (int i = arr.length - 1; i > -1; --i) {
            if (!result.isEmpty() && array.contains(arr[i] + result.get(0))) {
                result.remove(0);
            } else {
                result.add(0, arr[i]);
            }
        }
        return result.toArray(new String[result.size()]);
    }    


    public static String[] dirReduc_mine(String[] arr) {
        String str = String.join("", arr);
        str = str.replaceAll("NORTH", "N");
        str = str.replaceAll("SOUTH", "S");
        str = str.replaceAll("EAST", "E");
        str = str.replaceAll("WEST", "W");
        String[] patterns = { "NS", "EW", "SN", "WE" };

        boolean keepAlive = true;
        int before = 10000; 
        while ( keepAlive == true ) {
            for (String p : patterns) {
                str = str.replaceAll(p, "");
            }
            if ( str.length() < before ) {
                before = str.length();
            } else {
                keepAlive = false;
            }
        }

        char[] charArray = str.toCharArray();
        String raw = "";

        if (charArray.length == 0) {
            return new String[] {};
        }
        for (char c : charArray) {
            String s = String.valueOf(c);
            if (s.equals("N")) {
                raw += "NORTH ";
            } else if (s.equals("S")) {
                raw += "SOUTH ";
            } else if (s.equals("W")) {
                raw += "WEST ";
            } else if (s.equals("E")) {
                raw += "EAST ";
            }
        }
        String[] ary = raw.split(" ");
        return ary;
    }

    public static void main(String... string) {
        verdict(new String[] { "WEST" },
                dirReduc(new String[] { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" }));
        verdict(new String[] {}, dirReduc(new String[] { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH" }));


        verdict(new String[] { "EAST", "NORTH",   }, dirReduc(new String[] { "EAST", "EAST", "WEST", "NORTH", "WEST", "EAST", "EAST", "SOUTH", "NORTH", "WEST" }));

        


    }
}