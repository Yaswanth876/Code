#include <stdio.h>
int main ()
{
    char unit;
    float temp;
    printf ("\nIs the temperature in (C) or (F): ");
    scanf ("%c", &unit);
    if(unit == 'C')
    {
        printf ("\nEnter the temperature in Celsius: ");
        scanf ("%f", &temp);
        temp = (temp * 9 / 5) + 32; 
        printf ("\nThe temperature in Farenheit:%.1f", temp);
    }
    else if(unit == 'F')
    {
        printf ("\nEnte the temperature in Farenheit: ");
        scanf ("%f", &temp);
        temp = ((temp - 32) * 5) / 9;
        printf ("\nThe temperature in Celsius:%.1f",temp);
    }
    else
    {
        printf ("\n%c is not a valid unit of temperature", unit);
    }
    return 0;
}