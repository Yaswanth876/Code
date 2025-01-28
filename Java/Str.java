import java.security.MessageDigest;

public class Str {
    public static void main(String[] args) {
        String message = "Hello World!!";
        System.out.println(message.toLowerCase());
        System.out.println(message.toUpperCase());
        System.out.println(message.length());
        System.out.println(message.concat("Welcome to Java"));
        System.out.println(message.replace("!", "#"));
        System.out.println(message.compareTo("Hello"));
        System.out.println(message.endsWith("!"));
        System.out.println(message.startsWith("!"));
        System.out.println(message.replace("World", "Guys"));
        System.out.println(message);

    }
}