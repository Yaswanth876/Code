import java.util.Scanner;
public class TestArray {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int size = s.nextInt();
        int[] numbers = new int[size];
        int total = 0;
        System.out.printf("Enter %d elements\n", size);
        for(int i = 0; i < size; i++){
            System.out.printf("Enter number %d: ",i + 1);
            numbers[i] = s.nextInt();
        }
        for(int i = 0; i < size; i++){
            System.out.println(numbers[i] + " ");
        }
        for(int i = 0; i < size; i++){
            total += numbers[i];
        }
        int min = numbers[0];
        for(int i = 0; i < size; i++){
            if(min > numbers[i]) min = numbers[i];
        }
        int max = numbers[0];
        for(int i = 0; i < size; i++){
            if(max < numbers[i]) max = numbers[i];
        }
        System.out.println("The Total is " + total);
        System.out.println("The Maximum is " + max);
        System.out.println("The Minimum is " + min);
    }
}
