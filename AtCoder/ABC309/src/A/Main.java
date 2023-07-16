package A;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        
        final int A = Integer.parseInt(scanner.next());
        final int B = Integer.parseInt(scanner.next());

        if (B==4 || B==7) {
            System.out.println("No");
            return;
        }

        int difference = B-A;
        if (difference == 1) {
            System.out.println("Yes");
            return;
        } else {
            System.out.println("No");
            return;
        }
        
    }
}
