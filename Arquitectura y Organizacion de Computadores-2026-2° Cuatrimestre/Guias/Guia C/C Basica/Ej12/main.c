#include <stdio.h>

int main(){
    int s[4] = {1, 2, 3, 4};
    int nuevo_s[4] = {0 , 0, 0, 0};
    int shift = 0xCACA;
    for (int i = 0; i < 4; i++){
        nuevo_s[i] = s[(i + shift) % 4];
    }
    for (int i = 0; i < 4; i++) {
    printf("%d", nuevo_s[i]);
    if (i < 3) {
        printf(", ");
    }
} printf("\n");
}