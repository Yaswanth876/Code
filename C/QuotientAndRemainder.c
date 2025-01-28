#include <stdio.h>
int main (){
    int x, y, quotient, remainder;
    printf ("Enter two numbers: ");
    scanf ("%d %d",&x, &y);
    quotient = x / y;
    remainder = x % y;
    printf ("Quotient of %d and %d is %d", x, y, quotient);
    printf ("\nRemainder of %d and %d is %d", x, y, remainder);
    return 0;
}