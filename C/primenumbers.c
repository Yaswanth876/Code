#include<stdio.h>
int main()
{
    int n, flag;
    printf("Enter the range of the number: ");  
    scanf("%d", &n);
    printf("Prime numbers between 1 to %d are: ",n);
    for(int i=2; i<=n; i++)
    {
        flag = 1;
        for(int j=2; j*j<=i; j++)
        {
            if(i%j==0)
            {
                flag=0;
                break;
            }
        }
        if(flag)
            printf("%d ",i);
    }
    printf("\n");
    return 0;
}