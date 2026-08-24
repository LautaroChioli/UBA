#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char nombre[16];
    int edad;
} persona_t;

persona_t* crearPersona(char *nombre, int edad){
    persona_t *p = (persona_t*) malloc(20);
    int cont = 0;
    while (nombre[cont] != '\0'){
        (*p).nombre[cont] = nombre[cont];
        cont++;
    }
    (*p).edad = edad;
    return p;
}

int main(){
    persona_t *per1 = crearPersona("Crokus Younghand", 18);

    printf("Nombre: %s \n Edad: %d\n", (*per1).nombre, (*per1).edad);
    free(per1);
}