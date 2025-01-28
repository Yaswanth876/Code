#include <stdio.h>
int main ()
{
    float C, F;
    printf ("Enter the degree celsius: ");
    scanf ("%f",&C);
    F = (C * 1.8) + 32;
    printf ("\nCelsius to Farenheit");
    printf ("Farenheit = %f", F);
    C = (F - 32)*5/9;
    printf ("\nFarenheit to Celsius");
    printf ("Celsius = %f", C);
    return 0;
}