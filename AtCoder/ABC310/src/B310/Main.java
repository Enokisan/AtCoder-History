package B310;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        
        Scanner scanner = new Scanner(System.in);
        
        final int N = scanner.nextInt();
        final int M = scanner.nextInt();

        int[][] productMatrix = new int[N][(M+2)];
        for (int i=0; i<N; i++) {
            for (int j=0; j<2; j++) {
                productMatrix[i][j] = scanner.nextInt();
            }
            for (int j=0; j<productMatrix[i][1]; j++) {
                productMatrix[i][j+2] = scanner.nextInt();
            }
        }

        sort2DArrayBasedOnColumnNumber(productMatrix, 1);

        for (int i=0; i<N-1; i++) {
            ArrayList<Integer> iFeatureList = new ArrayList<Integer>();
            for (int j=0; j < productMatrix[i][1]; j++) {
                iFeatureList.add(productMatrix[i][j+2]);
            }

            for (int j=i+1; j<N; j++) {
                ArrayList<Integer> jFeatureList = new ArrayList<Integer>();
                for (int k=0; k < productMatrix[j][1]; k++) {
                    jFeatureList.add(productMatrix[j][k+2]);
                }

                if (iFeatureList.containsAll(jFeatureList)) {
                    if (productMatrix[i][0] < productMatrix[j][0] || productMatrix[i][1] > productMatrix[j][1]) {
                        System.out.println("Yes");
                        return;
                    }
                }
            }
        }

        System.out.println("No");
        return;
    }


    public static void sort2DArrayBasedOnColumnNumber (int[][] array, final int columnNumber){
        Arrays.sort(array, new Comparator<int[]>() {
            @Override
            public int compare(int[] first, int[] second) {
               if(first[columnNumber-1] > second[columnNumber-1]) return 1;
               else return -1;
            }
        });
    }
}
