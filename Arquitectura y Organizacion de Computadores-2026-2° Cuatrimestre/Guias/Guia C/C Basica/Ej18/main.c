#include <stdio.h>
#define FELIZ 0
#define TRISTE 1
int estado = TRISTE; 
void alcoholizar();
void print_estado();
int main(){
print_estado();
alcoholizar();
print_estado();
alcoholizar();alcoholizar();alcoholizar();
print_estado(); // que imprime?
}
void alcoholizar(){
int cantidad = 0; 
cantidad++;
if(cantidad < 3){
estado = FELIZ;
}else{
estado = TRISTE;
}
}
void print_estado(){
printf("Estoy %s\n", estado == FELIZ ? "feliz" : "triste");
}