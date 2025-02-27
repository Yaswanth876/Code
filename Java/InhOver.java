import java.util.Scanner;
class Vehicle {
    private String type;
    public Vehicle(String type){
        this.type=type;
    }
    public void startEngine(){
        System.out.println(type +" engine starts");
    }

    public void startEngin() {
    }
}
class Car extends Vehicle {
    public Car(){
        super("Car");
    }
    public void startEngine(){
        super.startEngine();
        System.out.println("Car starts with a roar");
    }
}
class Bike extends Vehicle {
    public Bike(){
        super("Bike");
    }
    public void startEngine(){
        super.startEngine();
        System.out.println("Bike starts with a vroom");
    }
}
class InhOver{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        System.out.print("Enter Vehicle type (C/B): ");
        String vehty = s.nextLine().trim().toLowerCase();
        Vehicle animal;
        if(vehty.equals("car")){
            animal = new Car();
        }else if(vehty.equals("bike")){
            animal = new Bike();
        }else{
            animal = new Vehicle("Generic Vehicle");
        }
        animal.startEngine();
    }
}
