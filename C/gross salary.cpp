#include <iostream>
using namespace std;
int main()
{
    float basic,gross,da,hra;
    cout<<"enter basic salary of an employee:";
    cin>>basic;
    if(basic<25000)
    {
     da=basic*80/100;
     hra=basic*20/100;
     }
     else if(basic>=25000&&basic<40000)
     {
      da=basic*90/100;
      hra=basic*25/100;
      }
      else if(basic>=40000)
      {
       da=basic*95/100;
       hra=basic*30/100;
       }
       gross=basic+hra+da;
       cout<<"  Basic Pay  :"<<basic<<endl;
       cout<<"  Dearness Allowance  :"<<da<<endl;
       cout<<"  House Rent Allowance  :"<<hra<<endl;
       cout<< "---------------------------"<<endl;
       cout<<"  Gross Salary  :"<<gross<<endl;
       cout<<"----------------------------"<<endl;
       return 0; 
