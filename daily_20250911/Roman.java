import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;

public class Roman {
    private LinkedHashMap<Integer, String> encoder;
    private LinkedHashMap<String, Integer> decoder;

    public Roman() {
        encoder = new LinkedHashMap<>();
        encoder.put(1000, "M");
        encoder.put(900, "CM");
        encoder.put(500, "D");
        encoder.put(400, "CD");
        encoder.put(100, "C");
        encoder.put(90, "XC");
        encoder.put(50, "L");
        encoder.put(40, "XL");
        encoder.put(10, "X");
        encoder.put(9, "IX");
        encoder.put(5, "V");
        encoder.put(4, "IV");
        encoder.put(1, "I");

        decoder = new LinkedHashMap<>();
        decoder.put("M", 1000);
        decoder.put("CM", 900);
        decoder.put("D", 500);
        decoder.put("CD", 400);
        decoder.put("C", 100);
        decoder.put("XC", 90);
        decoder.put("L", 50);
        decoder.put("XL", 40);
        decoder.put("X", 10);
        decoder.put("IX", 9);
        decoder.put("V", 5);
        decoder.put("IV", 4);
        decoder.put("I", 1);
    }

    public String encode(int num) {
        String result = "";
        for (Map.Entry<Integer, String> entry : encoder.entrySet()) {
            while (num >= entry.getKey()) {
                result += entry.getValue();
                num -= entry.getKey();
            }
        }
        return result;
    }

    public int decode(String num) throws IllegalArgumentException {
        int result = 0;
        int headIndex = 0;
        String parsedChars = "";
        for (Map.Entry<String, Integer> entry : decoder.entrySet()) {
            int headLength = entry.getKey().length();
            while (headIndex + headLength <= num.length()) {
                String head = num.substring(headIndex, headIndex + headLength);
                if (head.equals(entry.getKey())) {
                    result += entry.getValue();
                    parsedChars += head;
                    headIndex += headLength;
                } else {
                    break;
                }
            }
        }
        if (!parsedChars.equals(num)) {
            throw new IllegalArgumentException();
        }
        return result;
    }

    public static void main(String[] args) {
        Roman roman = new Roman();

        Scanner scan = new Scanner(System.in);
        System.out.print("整数またはローマ数字を入力: ");
        String input = scan.nextLine();
        scan.close();

        if (input.matches("\\d+")) {
            int num = Integer.parseInt(input);
            if (num < 4000 && num > 0) {
                System.out.println("ローマ数字: " + roman.encode(num));
            } else {
                System.out.println("値が不正です。変換できる値は 1 以上 4000 未満です。");
                System.exit(1);
            }
        } else if (input.matches("[MDCLXVI]+")) {
            try {
                System.out.println("整数: " + roman.decode(input));
            } catch (IllegalArgumentException e) {
                System.out.println("変換に失敗しました。");
                System.exit(1);
            }
        } else {
            System.out.println("入力が不正です。");
            System.exit(1);
        }
    }
}
