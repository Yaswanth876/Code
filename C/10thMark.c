#include <stdio.h>
int main ()
{
    int T, E, M, S, SS;
    int Total, a;
    float percent;
    printf ("Enter Tamil, English, Maths, Science, Social mark: ");
    scanf ("%d %d %d %d %d",&T,&E,&M,&S,&SS);
    printf ("\nTamil Mark  :%d",T);
    printf ("\nEnglish Mark:%d",E);
    printf ("\nMaths Mark  :%d",M);
    printf ("\nScience Mark:%d",S);
    printf ("\nSocial Mark :%d",SS);
    Total =T+E+M+S+SS;
    printf ("\nTotal = %d / 500",Total);
    percent = Total / 5;
    printf ("\nPercentage = %.1f", percent);
    return 0;
}