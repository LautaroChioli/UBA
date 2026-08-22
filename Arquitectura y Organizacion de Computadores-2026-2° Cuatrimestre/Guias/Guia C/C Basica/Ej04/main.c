#include <stdio.h>
#include <stdint.h>


int main() {
    int8_t a = 126;
    int16_t b = 128;
    int32_t c = 2147483646;
    int64_t d = 2147483648;


    printf("int8(%lu): %d \n", sizeof(a), a);
    printf("int16(%lu): %d \n", sizeof(b), b);
    printf("int32(%lu): %d \n", sizeof(c), c);
    printf("int64(%lu): %ld \n", sizeof(d), d);



}