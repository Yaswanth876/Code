#include <stdio.h>
int main (){
    int a, b;
    printf ("Enter a : ");
    scanf ("%d",&a);
    printf ("Enter b : ");
    scanf ("%d",&b);
    printf ("Values before swaping\n");
    printf ("a = %d\t",a);
    printf ("b = %d\n",b);
    a = a - b;
    b = a + b;
    a = b - a;
    printf ("Values after swaping\n");
    printf ("a = %d\t",a);
    printf ("b = %d",b);
    return 0;

}