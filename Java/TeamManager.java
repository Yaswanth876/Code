import java.util.ArrayList;
import java.util.Scanner;

public class TeamManager {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> players = new ArrayList<>();
        System.out.println("Enter the team name: ");
        String teamName = sc.nextLine();
        // Asking user for the number of players
        System.out.print("Enter the number of players: ");
        int size = sc.nextInt();
        sc.nextLine(); // Consume newline

        // Getting player names
        System.out.println("Enter player names");
        for (int i = 0; i < size; i++) {
            System.out.print("Player"+(i+1)+": ");
            players.add(sc.nextLine());
        }
        System.out.println(" ");
        System.out.println("Team Name: "+teamName);
        // Displaying student names using for-each loop
        System.out.println("Players List:");
        for (String player : players) {
            System.out.println(player);
        }

        sc.close();
    }
}
