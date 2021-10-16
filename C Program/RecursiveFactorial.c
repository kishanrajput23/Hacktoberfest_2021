/* 
------------------------------------------------------------------------------------------------
DESCRIPTION: THIS IS A PROGRAM TO FIND THE FACTORIAL OF A NUMBER IN A RECURSIVE WAY
------------------------------------------------------------------------------------------------
*/

#include<stdio.h>
long int product(int n);
int main() {
    int n;
    printf("Enter a positive integer: ");
    scanf("%d",&n);
    printf("Factorial of %d = %ld", n, produt(n));
    return 0;
}

long int product(int n) {
    if (n>=1)
        return n*procuct(n-1);
    else
        return 1
