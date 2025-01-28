#include <stdio.h>
int main ()
{
    int b, h, area;
    printf ("Enter Base and Height of the triangle: ");
    scanf ("%d %d", &b, &h);
    area = (b * h)/ 2;
    printf ("The area of the triangle is %d meter square",area);
    return 0;
}