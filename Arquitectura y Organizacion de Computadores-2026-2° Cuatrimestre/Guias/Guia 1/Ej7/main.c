#include <stdio.h>



int main() {
    int a = 5;
    int b = 3;
    int c = 2;
    int d = 1;

    float res1 = a + b * c / d;
    printf(" a + b * c / d = %f\n", res1);
    res1 = a % b;
    printf("a %% b = %f\n", res1);
    int res2 = a == b;
    printf("a == b = %d\n ", res2);  
    res2 = a != b;
    printf("a != b = %d\n", res2);
    res2 = a & b;
    printf("a & b = %d\n", res2);
     printf("a & b = %b\n", res2);
    res2 = a | b;
    printf("a | b = %d \n", res2);
     printf("a | b = %b\n", res2);
    res2 = ~a;
    printf("~a = %d\n", res2);
     printf("~a = %b\n", res2);
    res2 = a && b;
    printf("a && b = %d\n", res2);
    res2 = a || b;
    printf("a || b = %d\n", res2);
    res2 = a << 1;
    printf("a << 1 = %d\n", res2);
    printf("a << 1 = %b\n", res2);
    res2 = a >> 1;
    printf("a >> 1 = %d\n", res2);
    printf("a >> 1 = %b\n", res2);
    res2 =  a += b;
    printf(" a += b = %d\n", res2);

}