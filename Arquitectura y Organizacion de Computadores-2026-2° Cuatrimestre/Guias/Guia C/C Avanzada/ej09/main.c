#include <stdio.h>

char all_caps(char *str);

int main(){
    char str[] = "Mr. Bungle!\n";
    all_caps(str);
    printf("%s", str);
}

char all_caps(char *str){
    while (*str != '\0'){
        if (*str >= 'a' && *str <= 'z'){
              *str -= 32;
        }
        str++;
    }
}