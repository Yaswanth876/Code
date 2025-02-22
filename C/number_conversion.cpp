#include <iostream>
#include <cmath>
using namespace std ;
int main()
{
  int dec,d,i,temp,ch;
  long int bin;
  do  
  {
   dec=bin=d=i=0;
   cout<<"\n\n\t\tMENU\n1.Decimal number to binary number\n2.Binary to decimal number\n3.Exit\n";
   cout<<"enter your choice(1/2/3)";
   cin>>ch;
   switch(ch)
   {
    case 1:
    cout<<"enter a decimal number:";
    cin>>dec;
    temp=dec;
    while(dec!=0)
    {
    d=dec%2;
    bin+=d*pow(10,i);
    dec/=2;
}
cout<<temp<<"in decimal"<<bin<<"in binary"<<endl;
break;
case 2:
  cout<<"enter a binary :";
  cin>>bin;
  temp=bin;
  while(bin!=0)
  {
   d=bin%10;
   dec+=d*pow(2,i);
   bin/=2;
}
cout<<temp<<"in binary"<<dec<<"in decimal";
break;
case 3:
break;
default:
 cout<<"invalid choice";
}
}while(ch!=3);
return 0;
}

