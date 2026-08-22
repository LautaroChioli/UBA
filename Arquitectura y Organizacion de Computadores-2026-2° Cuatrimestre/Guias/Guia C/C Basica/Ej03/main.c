#include <stdio.h>
#include <stdbool.h>


int main() {
    char a = 12;
    short b = -8100;
    int c = 123456;
    long d = 123456789011;

    float flt = 3.14;
    double dbl = 3.141592653589793;
    long double ld = 3.14159265358979323;

    printf("char(%lu): %d \n", sizeof(a), a);
    printf("short(%lu): %d \n", sizeof(b), b);
    printf("int(%lu): %d \n", sizeof(c), c);
    printf("long(%lu): %ld \n", sizeof(d), d);
    printf("float(%lu): %f \n", sizeof(flt), flt);
    printf("double(%lu): %.15f \n", sizeof(dbl), dbl);
    printf("long double(%lu): %.18LF \n", sizeof(ld), ld);


}