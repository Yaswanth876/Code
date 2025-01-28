#include <stdio.h>
int main (){
    int a, b, temp;
    printf ("Enter a: ");
    scanf ("%d",&a);
    printf ("Enter b: ");
    scanf ("%d",&b);
    printf ("Before Swaping\n");
    printf ("a = %d\t",a);
    printf ("b = %d\n",b);
    temp = a;
    a = b;
    b = temp;
    printf ("After Swapnig\n");
    printf ("a = %d\t",a);
    printf ("b = %d",b);
    return 0;

}