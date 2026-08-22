#include <stdio.h>

int fact(int n);

int main(){
    int n = 12;

    n = fact(n);

    printf("%d\n", n);
}

int fact(int n){
    if (n == 0){
        return 1;
    }

    int sum = n;

    while (n > 1){
        n-- ;
        sum *= n;
    }
    return sum;
}