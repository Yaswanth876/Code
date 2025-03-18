import java.io.*;
import java.util.Scanner;

// Football Player Class (Serializable)
class FootballPlayer implements Serializable {
    private String name, team;
    private int jersey;

    public FootballPlayer(String name, String team, int jersey) {
        this.name = name;
        this.team = team;
        this.jersey = jersey;
    }

    public void showInfo() {
        System.out.println(name + " | " + team + " | Jersey No: " + jersey);
    }
}

public class FootballSerialization {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String filename = "player.ser";

        // User Input
        System.out.print("Enter Player Name: ");
        String name = sc.nextLine();
        System.out.print("Enter Team Name: ");
        String team = sc.nextLine();
        System.out.print("Enter Jersey Number: ");
        int jersey = sc.nextInt();

        // Creating player object
        FootballPlayer player = new FootballPlayer(name, team, jersey);

        // Serialization (Saving Object)
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(filename))) {
            out.writeObject(player);
            System.out.println("Player Data Saved!");
        } catch (IOException e) {
            System.out.println("Save Error: " + e.getMessage());
        }

        // Deserialization (Loading Object)
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(filename))) {
            System.out.println("Loaded Player Data:");
            ((FootballPlayer) in.readObject()).showInfo();
        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Load Error: " + e.getMessage());
        }

        sc.close();
    }
}
