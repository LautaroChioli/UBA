#include <stdio.h>
#include <stdlib.h>

int main(){
    int tiradas[] = {0, 0, 0, 0, 0, 0};
    for (int i = 0; i < 60000001; i++){
        int dado = rand() % 6;
        tiradas[dado]++;
    }
    for (int i = 0; i < 6; i++) {
    printf("%d", tiradas[i]);
    if (i < 5) {
        printf(", ");
    }
} printf("\n");
}