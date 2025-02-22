import java.util.Scanner;

class Operation {
    public int add(int n1, int n2) {
        return n1 + n2;
    }

    public int sub(int n1, int n2) {
        return n1 - n2;
    }

    public int multiply(int n1, int n2) {
        return n1 * n2;
    }

    public int divide(int n1, int n2) {
        return n1 / n2;
    }
}

@SuppressWarnings("unused")
class Arithmetic {
    public static void main(String[] args) {
        try (Scanner s = new Scanner(System.in)) {
            while (true) {
                System.out.println("Operations");
                System.out.println("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit");
                System.out.print("Enter your choice: ");
                int choice = s.nextInt();
                if (choice == 5) {
                    System.out.println("Exited...");
                    break;
                }
                System.out.print("Enter first number: ");
                int a = s.nextInt();
                System.out.print("Enter second number: ");
                int b = s.nextInt();
                Operations op = new Operations();
                switch (choice) {
                    case 1 -> System.out.println("The Sum is " + op.add(a, b));
                    case 2 -> System.out.println("The Difference is " + op.sub(a, b));
                    case 3 -> System.out.println("The Multiplication is " + op.multiply(a, b));
                    case 4 -> {
                        if (b != 0) {
                            System.out.println("The Division is " + op.divide(a, b));
                        } else {
                            System.out.println("Zero can't be a divisor");
                        }
                    }
                    default -> System.out.println("Invalid choice");
                }
            }
            // Close the scanner to prevent resource leak
        }
    }
}

class Operations {
    public int add(int n1, int n2) {
        return n1 + n2;
    }

    public int sub(int n1, int n2) {
        return n1 - n2;
    }

    public int multiply(int n1, int n2) {
        return n1 * n2;
    }

    public int divide(int n1, int n2) {
        return n1 / n2;
    }
}

class Calculator {
    public static void main(String[] args) {
        try (Scanner s = new Scanner(System.in)) {
            while (true) {
                System.out.println("Operations");
                System.out.println("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit");
                System.out.print("Enter your choice: ");
                int choice = s.nextInt();
                if (choice == 5) {
                    System.out.println("Exited...");
                    break;
                }
                System.out.print("Enter first number: ");
                int a = s.nextInt();
                System.out.print("Enter second number: ");
                int b = s.nextInt();
                Operations op = new Operations();
                switch (choice) {
                    case 1 -> System.out.println("The Sum is " + op.add(a, b));
                    case 2 -> System.out.println("The Difference is " + op.sub(a, b));
                    case 3 -> System.out.println("The Multiplication is " + op.multiply(a, b));
                    case 4 -> {
                        if (b != 0) {
                            System.out.println("The Division is " + op.divide(a, b));
                        } else {
                            System.out.println("Zero can't be a divisor");
                        }
                    }
                    default -> System.out.println("Invalid choice");
                }
            }
            // Close the scanner to prevent resource leak
        }
    }
}

