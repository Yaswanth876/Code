#include <stdio.h>
int main (){
    int intType;
    float floatType;
    double doubleType;
    char charType;
    printf("Size of Int data type is %zu\n",sizeof(intType));
    printf("Size of Float data type is %zu\n",sizeof(floatType));
    printf("Size of Double data type is %zu\n",sizeof(doubleType));
    printf("Size of Char data type is %zu\n",sizeof(charType));
    return 0;
}