import java.util.Scanner;
abstract class Shape{
    double dim1, dim2;
    Shape(double d1, double d2){
        dim1 = d1;
        dim2 = d2;
    }
    abstract double area();
}
class Rectangle extends Shape{
    Rectangle(double d1, double d2){
        super(d1, d2);
    }
    double area(){
        return dim1*dim2;
    }
}
class Triangle extends Shape{
    Triangle(double d1, double d2){
        super(d1, d2);
    }
    double area(){
        return dim1*dim2*0.5;
    }
}
class Abs{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        System.out.print("Enter the dimensions: ");
        double d1 = s.nextDouble();
        double d2 = s.nextDouble();
        Rectangle r = new Rectangle(d1, d2);
        System.out.print("Area of rectangle: "+ r.area());
        Triangle t = new Triangle(d1, d2);
        System.out.print("\nArea of Triangle: "+ t.area());
    }
}