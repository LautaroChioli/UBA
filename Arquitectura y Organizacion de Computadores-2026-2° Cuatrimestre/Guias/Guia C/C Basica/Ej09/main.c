#include <stdio.h>

int main (){
    __uint32_t a = 0x40000000;
    __uint32_t b = 0xA0000002;

    __uint32_t topmask = 0xE0000000;
    __uint32_t bottommask = 0x00000007 ;

    __uint32_t top_a = a & topmask;
    __uint32_t top_a_shifted = top_a >> 29;

    __uint32_t bottom_b = b & bottommask;

    printf("%b, %b\n", top_a_shifted, bottom_b);
    if (bottom_b == top_a_shifted) {
        printf("Iguales: %d = %d\n", top_a_shifted, bottom_b);
    }
    if (bottom_b > top_a_shifted) {
        printf("bottom_b es mayor que top_a: %d > %d\n", bottom_b, top_a_shifted);
    }
    if (bottom_b < top_a_shifted){
        printf("bottom_b es menor que top_a: %d < %d\n", bottom_b, top_a_shifted);
    }

}