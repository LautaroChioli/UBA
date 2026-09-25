#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <assert.h>

#include "../test-utils.h"
#include "Estructuras.h"

int main() {
	lista_t lista_vacia;
    lista_vacia.head = NULL;
    
    assert(cantidad_total_de_elementos(&lista_vacia) == 0);
    printf("[OK] Lista normal vacia -> 0 elementos.\n");

    // ---------------------------------------------------------
    // TEST 2: Lista normal con 3 elementos
    // ---------------------------------------------------------
    nodo_t n3;
    n3.next = NULL;
    
    nodo_t n2;
    n2.next = &n3;
    
    nodo_t n1;
    n1.next = &n2;
    
    lista_t lista_llena;
    lista_llena.head = &n1;

    assert(cantidad_total_de_elementos(&lista_llena) == 3);
    printf("[OK] Lista normal llena -> 3 elementos.\n");

    // ---------------------------------------------------------
    // TEST 3: Lista empaquetada (packed) vacía
    // ---------------------------------------------------------
    packed_lista_t p_lista_vacia;
    p_lista_vacia.head = NULL;

    assert(cantidad_total_de_elementos_packed(&p_lista_vacia) == 0);
    printf("[OK] Lista packed vacia -> 0 elementos.\n");

    // ---------------------------------------------------------
    // TEST 4: Lista empaquetada (packed) con 2 elementos
    // ---------------------------------------------------------
    packed_nodo_t pn2;
    pn2.next = NULL;
    
    packed_nodo_t pn1;
    pn1.next = &pn2;

    packed_lista_t p_lista_llena;
    p_lista_llena.head = &pn1;

    assert(cantidad_total_de_elementos_packed(&p_lista_llena) == 2);
    printf("[OK] Lista packed llena -> 2 elementos.\n");

    printf("\n¡Todos los tests pasaron exitosamente!\n");
    return 0;
}
