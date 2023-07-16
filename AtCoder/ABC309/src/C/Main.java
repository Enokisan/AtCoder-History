package C;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        final int N = scanner.nextInt();
        final int K = scanner.nextInt();

        long[][] abMatrix = new long[N][2];
        long sumOfB = 0;
        for (int i=0; i<N; i++) {
            for (int j=0; j<2; j++) {
                abMatrix[i][j] = scanner.nextLong();
                if (j==1) {
                    sumOfB += abMatrix[i][j];
                }
            }
        }

        Sort2DArrayBasedOnColumnNumber(abMatrix, 1);

        if (sumOfB <= K) {
            System.out.println(1);
            return;
        }

        for (int row=0; row<N; row++) {
            sumOfB -= abMatrix[row][1];           
            if (sumOfB <= K) {
                System.out.println(abMatrix[row][0]+1);
                return;
            }
        }

    }


    public static void Sort2DArrayBasedOnColumnNumber (long[][] array, final int columnNumber){
        Arrays.sort(array, new Comparator<long[]>() {
            @Override
            public int compare(long[] first, long[] second) {
               if(first[columnNumber-1] > second[columnNumber-1]) return 1;
               else return -1;
            }
        });
    }
}
