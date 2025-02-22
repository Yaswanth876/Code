class MethodOverloading{
    public int add(int a, int b){
        return a+b;
    }
    public int add(int a, int b, int c){
        return a+b+c;
    }
}
class ConstructorOverloading{
    int num1,num2;
    ConstructorOverloading(){
        num1 = -1;
        num2 = -1;
    }
    ConstructorOverloading(int a, int b){
        num1 = a;
        num2 = b;
    }
    void display(){
        System.out.println("Num1: "+ num1);
        System.out.println("Num2: "+ num2);
    }
}
class Overloading {
    public static void main(String[] args){
        MethodOverloading mo = new MethodOverloading();
        System.out.println("Sum1: "+ mo.add(10,20));
        System.out.println("Sum2: "+ mo.add(10,20,30));
        ConstructorOverloading co1 = new ConstructorOverloading();
        ConstructorOverloading co2 = new ConstructorOverloading(10,20);
        co1.display();
        co2.display();
    }

}
