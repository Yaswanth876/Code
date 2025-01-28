#include <stdio.h>
int main ()
{
    const double PI = 3.14159;
    double radius, circumference, area;
    printf ("Enter the radius of the circle: ");
    scanf ("%lf",&radius);
    circumference = 2 * PI * radius;
    area = PI * radius * radius;
    printf ("Circimference of the circle is %lf",circumference);
    printf ("\nArea of the circle is %lf", area);
    return 0;

}