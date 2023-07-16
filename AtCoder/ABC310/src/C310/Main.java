package C310;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);

        final int N = scanner.nextInt();

        ArrayList<String> sList = new ArrayList<String>();
        for (int i=0; i<N; i++) {
            sList.add(scanner.next());
        }
        sList.sort(Comparator.comparingInt(String::length));

        for (int i=0; i<N; i++) {
            if (sList.get(i).length() == sList.get(i+1).length()) {
                
            }
        }
        

        for (int i=0; i<N; i++) {
            System.out.println(sList.get(i));
        }

    }

    // `Collections.reverse()`を使用してJavaで文字列を反転するメソッド
    public static String reverse(String str)
    {
        //基本ケース：文字列がnullまたは空の場合
        if (str == null || str.equals("")) {
            return str;
        }
 
        //文字の空のリストを作成します
        List<Character> list = new ArrayList<Character>();
 
        //指定された文字列のすべての文字をその文字列にプッシュします
        for (char c: str.toCharArray()) {
            list.add(c);
        }
 
        //`java.util.Collections`を使用してリストを逆にします`reverse()`
        Collections.reverse(list);
 
        //`StringBuilder`を使用して`ArrayList`を文字列に変換して返します
        StringBuilder builder = new StringBuilder(list.size());
        for (Character c: list) {
            builder.append(c);
        }
 
        return builder.toString();
    }
}
