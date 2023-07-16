package B;

import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        final int N = scanner.nextInt();

        char[][] aMatrix = new char[N][N];
        for (int i=0; i<N; i++) {
            aMatrix[i] = scanner.next().toCharArray();
        }

        char[][] bMatrix = new char[N][N];
        for (int i=0; i<N; i++) {
            bMatrix[i] = aMatrix[i].clone();
        }
        

        for (int i=1; i<N; i++) {
            bMatrix[0][i] = aMatrix[0][i-1];
        }

        for (int i=1; i<N; i++) {
            bMatrix[i][N-1] = aMatrix[i-1][N-1];
        }

        for (int i=N-2; i>=0; i--) {
            bMatrix[N-1][i] = aMatrix[N-1][i+1];
        }

        for (int i=N-2; i>=0; i--) {
            bMatrix[i][0] = aMatrix[i+1][0];
        }



        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                System.out.print(bMatrix[i][j]);
            }
            System.out.println();
        }
    }
}
