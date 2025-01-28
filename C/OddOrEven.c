#include<stdio.h>
int check(int n)
{
    if(n%2==0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int main()
{
    int n;
    printf("Enter the number: ");
    scanf("%d", &n);
    if(check(n))
    {
        printf("The number is even");
    }
    else
    {
        printf("The number is odd");
    }
    return 0;
}