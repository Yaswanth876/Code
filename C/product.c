#include <stdio.h>
int main (){
    double x, y, product;
    printf ("Enter two numbers:");
    scanf ("%lf %lf",&x,&y);
    product = x * y;
    printf ("The product of %lf and %lf is %.3lf",x,y,product);
    return 0;
}