

;########### ESTOS SON LOS OFFSETS Y TAMAÑO DE LOS STRUCTS
; Completar las definiciones (serán revisadas por ABI enforcer):
%define NODO_OFFSET_NEXT 0
%define NODO_OFFSET_CATEGORIA 8
%define NODO_OFFSET_ARREGLO 16
%define NODO_OFFSET_LONGITUDW 24
%define NODO_SIZE 32
%define PACKED_NODO_OFFSET_NEXT 0
%define PACKED_NODO_OFFSET_CATEGORIA 8
%define PACKED_NODO_OFFSET_ARREGLO 9
%define PACKED_NODO_OFFSET_LONGITUD 17
%define PACKED_NODO_SIZE 21
%define LISTA_OFFSET_HEAD 0
%define LISTA_SIZE 8
%define PACKED_LISTA_OFFSET_HEAD 0
%define PACKED_LISTA_SIZE 8

;########### SECCION DE DATOS
section .data

;########### SECCION DE TEXTO (PROGRAMA)
section .text

;########### LISTA DE FUNCIONES EXPORTADAS
global cantidad_total_de_elementos
global cantidad_total_de_elementos_packed

;########### DEFINICION DE FUNCIONES
;extern uint32_t cantidad_total_de_elementos(lista_t* lista);
;registros: lista[?]
cantidad_total_de_elementos:
	XOR EAX, EAX

	.loop:

	CMP RDI, 0
	JE .fin 
	INC EAX
	MOV RDI, [RDI + NODO_OFFSET_NEXT]
	JMP .loop 


	.fin:

	ret

;extern uint32_t cantidad_total_de_elementos_packed(packed_lista_t* lista);
;registros: lista[?]
cantidad_total_de_elementos_packed:
	XOR EAX, EAX

	.loop2:

	CMP RDI, 0
	JE .fin2

	INC EAX

	MOV RDI, [RDI + PACKED_NODO_OFFSET_NEXT]

	JMP .loop2

	.fin2: 
	ret

