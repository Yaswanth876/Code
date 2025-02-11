import java.util.Scanner;
public class TestMatrix {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        System.out.println("Enter size of the matrix: ");
        int size = s.nextInt();
        int[][] mat1, mat2, sum;
        mat1 = new int[size][size];
        mat2 = new int[size][size];
        sum = new int[size][size];
        System.out.println("Enter array elements");
        for(int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                System.out.printf("Enter number [%d][%d]: ", i ,j);
                mat1[i][j] = s.nextInt();
            }
        }
            for(int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    System.out.printf("Enter number [%d][%d]: ", i , j);
                    mat2[i][j] = s.nextInt();

                }
            }
    }
}
