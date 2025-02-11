#include<stdio.h>
#include<stdlib.h>
int main()
{
 	int num1,num2,lcm,max;
 	printf("Enter first number: ");
 	scanf("%d",&num1);
 	printf("Enter second number: ");
	scanf("%d",&num2);
	max = num1 > num2 ? num1 : num2;
	lcm = max;
	while(1)
	{
	 	if(lcm % num1 == 0 || lcm % num2 == 0){
			   printf("The LCM of %d and %d is %d.",num1,num2,lcm);
			   break;
         }
         lcm = max + 1;
    }
}
		     
