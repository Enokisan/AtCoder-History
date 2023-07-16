package A310;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);

        final int N = scanner.nextInt();
        final int P = scanner.nextInt();
        final int Q = scanner.nextInt();
        ArrayList<Integer> dArray = new ArrayList<Integer>();
        
        for (int i=0; i<N; i++) {
            dArray.add(scanner.nextInt());
        }

        if (P < Collections.min(dArray) + Q) {
            System.out.println(P);
            return;
        } else {
            System.out.println(Collections.min(dArray) + Q);
        }

    }
}
