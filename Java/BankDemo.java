import java.util.Scanner;

class BankAccount {
    private double balance;

    public BankAccount(double balance) {
        this.balance = balance;
    }

    public void withdraw(double amount) {
        try {
            if (amount > balance) {
                throw new Exception("Insufficient funds!");
            }
            balance -= amount;
            System.out.println("Withdrawn ₹" + amount + ". Remaining Balance: ₹" + balance);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}

public class BankDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // User input
        System.out.print("Enter initial balance: ");
        double balance = sc.nextDouble();
        System.out.print("Enter withdrawal amount: ");
        double amount = sc.nextDouble();

        // Creating account and withdrawing
        BankAccount account = new BankAccount(balance);
        account.withdraw(amount);

        sc.close();
    }
}
