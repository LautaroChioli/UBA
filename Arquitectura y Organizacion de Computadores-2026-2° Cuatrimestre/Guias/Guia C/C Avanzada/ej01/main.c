#include <stdio.h>

typedef struct {
    char nombre[8];
    int vida;
    double ataque;
    double defensa;
} monstruo_t;

void print_mon(monstruo_t);
static int cont = 1;

int main(){
    monstruo_t mon1 = {"Fiddler", 100, 10, 10};
    monstruo_t mon2 = {"Crokus", 120, 5, 15};
    monstruo_t mon3 = {"Apsalar", 50, 20, 5};
    print_mon(mon1);
    print_mon(mon2);
    print_mon(mon3);
    return 0;
}

void print_mon(monstruo_t mon){
    printf("Monstruo numero %d:\n", cont);
    printf("Nombre: %s\n", mon.nombre);
    printf("Vida: %d\n", mon.vida);
    printf("Ataque: %f\n", mon.ataque);
    printf("Defensa: %f\n", mon.defensa);
    cont++;
}
