import java.util.Scanner;
class Animal{
    private String animalName;
    public Animal(String animalName){
        this.animalName = animalName;
    }
    public void eats(){
        System.out.println(animalName +" start to eat");
    }
}
class Cat extends Animal {
    public Cat(){
        super("Cat");
    }
    public void eats(){
        super.eats();
        System.out.println("Cat eats fish");
    }
}
class Dog extends Animal {
    public Dog(){
        super("Dog");
    }
    public void eats(){
        super.eats();
        System.out.println("Dog eats bone");
    }
}
class InheritanceOverriding{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        System.out.print("Enter your pet (C/D): ");
        String pet = s.nextLine().trim().toLowerCase();
        Animal animal;
        if(pet.equals("cat")){
            animal = new Cat();
        }else if(pet.equals("dog")){
            animal = new Dog();
        }else{
            animal = new Animal("Generic Animal");
        }
        animal.eats();
    }
}
