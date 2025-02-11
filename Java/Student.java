<<<<<<< HEAD
import java.util.Scanner;

class Student {
    String name;
    int age;

    // Constructor
    Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Method to display student details
    void display() {
        System.out.println("Name: " + name + ", Age: " + age);
    }

    // Method to modify student details and return a new object
    static Student modifyStudent(Student s) {
        return new Student(s.name + " Updated", s.age + 1);
    }

    // Method to process an array of Student objects
    static void processStudents(Student[] students) {
        for (Student s : students) {
            s.display();
        }
    }

    public static void main(String[] args) {
        // Taking input for a single student
        try (Scanner scanner = new Scanner(System.in)) {
            // Taking input for a single student
            System.out.print("Enter student name: ");
            String name = scanner.nextLine();
            System.out.print("Enter student age: ");
            int age = scanner.nextInt();
            scanner.nextLine();  // Consume the newline character

            Student s1 = new Student(name, age);
            Student s2 = modifyStudent(s1);
            System.out.println("Modified Student:");
            s2.display();
            
            // Taking input for an array of students
            System.out.print("Enter the number of students: ");
            int n = scanner.nextInt();
            scanner.nextLine();  // Consume the newline character
            
            Student[] studentArray = new Student[n];
            
            for (int i = 0; i < n; i++) {
                System.out.print("Enter name for student " + (i + 1) + ": ");
                String studentName = scanner.nextLine();
                System.out.print("Enter age for student " + (i + 1) + ": ");
                int studentAge = scanner.nextInt();
                scanner.nextLine();  // Consume the newline character
                studentArray[i] = new Student(studentName, studentAge);
            }
            
            System.out.println("\nProcessing Student List:");
            processStudents(studentArray);
        }
    }
}
=======
import java.util.Scanner;

class Student {
    String name;
    int age;

    // Constructor
    Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Method to display student details
    void display() {
        System.out.println("Name: " + name + ", Age: " + age);
    }

    // Method to modify student details and return a new object
    static Student modifyStudent(Student s) {
        return new Student(s.name + " Updated", s.age + 1);
    }

    // Method to process an array of Student objects
    static void processStudents(Student[] students) {
        for (Student s : students) {
            s.display();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Taking input for a single student
        System.out.print("Enter student name: ");
        String name = scanner.nextLine();
        System.out.print("Enter student age: ");
        int age = scanner.nextInt();
        scanner.nextLine();  // Consume the newline character

        Student s1 = new Student(name, age);
        Student s2 = modifyStudent(s1);
        System.out.println("Modified Student:");
        s2.display();

        // Taking input for an array of students
        System.out.print("Enter the number of students: ");
        int n = scanner.nextInt();
        scanner.nextLine();  // Consume the newline character

        Student[] studentArray = new Student[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Enter name for student " + (i + 1) + ": ");
            String studentName = scanner.nextLine();
            System.out.print("Enter age for student " + (i + 1) + ": ");
            int studentAge = scanner.nextInt();
            scanner.nextLine();  // Consume the newline character
            studentArray[i] = new Student(studentName, studentAge);
        }

        System.out.println("\nProcessing Student List:");
        processStudents(studentArray);

        scanner.close();
    }
}
>>>>>>> 68decb54c26a046ca6acb5621d843a19b4091149
