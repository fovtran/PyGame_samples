/*C program to swap two nibbles of a given byte*/

#include <stdio.h>
/* function : swapTwoNibbles, to swap two nibbles of a given byte.*/
unsigned char swapTwoNibbles(unsigned char n)
{
    unsigned char num;
    num= ( (n & 0x0F)<<4 | (n & 0xF0)>>4 );
    return num;
}

int main()
{
    unsigned char number;
    unsigned char revNumber;
    printf("Enter an integer number (One byte number):");
    scanf("%u",&number);

    revNumber=swapTwoNibbles(number);
    printf("\nEntered Number was : %u \nNumber after swapping nibbles : %u",number,revNumber);

    return 0;
}
