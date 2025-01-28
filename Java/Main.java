class Calculator{
    public int add(int num1, int num2){
        return num1 + num2;
    }
}
public class Main {
    public static void main(String[] args){
        Calculator calc = new Calculator();
        int result = calc.add(20,8);
        System.out.println("The Sum is "+ result);
    }

}
