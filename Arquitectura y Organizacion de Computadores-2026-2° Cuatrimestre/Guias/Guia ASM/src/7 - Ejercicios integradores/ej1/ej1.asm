extern malloc

section .rodata
; Acá se pueden poner todas las máscaras y datos que necesiten para el ejercicio

section .text
; Marca un ejercicio como aún no completado (esto hace que no corran sus tests)
FALSE EQU 0
; Marca un ejercicio como hecho
TRUE  EQU 1

; Marca el ejercicio 1A como hecho (`true`) o pendiente (`false`).
;
; Funciones a implementar:
;   - es_indice_ordenado
global EJERCICIO_1A_HECHO
EJERCICIO_1A_HECHO: db TRUE; Cambiar por `TRUE` para correr los tests.

; Marca el ejercicio 1B como hecho (`true`) o pendiente (`false`).
;
; Funciones a implementar:
;   - indice_a_inventario
global EJERCICIO_1B_HECHO
EJERCICIO_1B_HECHO: db TRUE; Cambiar por `TRUE` para correr los tests.

;########### ESTOS SON LOS OFFSETS Y TAMAÑO DE LOS STRUCTS
; Completar las definiciones (serán revisadas por ABI enforcer):
ITEM_NOMBRE_OFFSET EQU 0
ITEM_FUERZA_OFFSET EQU 20
ITEM_DURABILIDAD_OFFSET EQU 24

;; La funcion debe verificar si una vista del inventario está correctamente 
;; ordenada de acuerdo a un criterio (comparador)

;; bool es_indice_ordenado(item_t** inventario, uint16_t* indice, uint16_t tamanio, comparador_t comparador);

;; Dónde:
;; - `inventario`: Un array de punteros a ítems que representa el inventario a
;;   procesar.
;; - `indice`: El arreglo de índices en el inventario que representa la vista.
;; - `tamanio`: El tamaño del inventario (y de la vista).
;; - `comparador`: La función de comparación que a utilizar para verificar el
;;   orden.
;; 
;; Tenga en consideración:
;; - `tamanio` es un valor de 16 bits. La parte alta del registro en dónde viene
;;   como parámetro podría tener basura.
;; - `comparador` es una dirección de memoria a la que se debe saltar (vía `jmp` o
;;   `call`) para comenzar la ejecución de la subrutina en cuestión.
;; - Los tamaños de los arrays `inventario` e `indice` son ambos `tamanio`.
;; - `false` es el valor `0` y `true` es todo valor distinto de `0`.
;; - Importa que los ítems estén ordenados según el comparador. No hay necesidad
;;   de verificar que el orden sea estable.


INDICE_OFFSET EQU 2
global es_indice_ordenado
es_indice_ordenado:
	; Te recomendamos llenar una tablita acá con cada parámetro y su
	; ubicación según la convención de llamada. Prestá atención a qué
	; valores son de 64 bits y qué valores son de 32 bits o 8 bits.
	;
	; r/m64 = item_t**     inventario
	; r/m64 = uint16_t*    indice
	; r/m16 = uint16_t     tamanio
	; r/m64 = comparador_t comparador
	PUSH rbp
	mov rbp, rsp
	PUSH r12
	PUSH r13
	PUSH r14
	PUSH r15
	PUSH rbx
	SUB rsp, 8

	MOV r12, rdi
	MOV r13, rsi
	MOVZX r14, dx
	MOV r15, rcx
	XOR rbx, rbx
	SUB r14, 1

	.loop:
	XOR r8, r8
	XOR r9, r9
	MOV r8w, [r13 + rbx * INDICE_OFFSET]
	MOV r9w, [r13 + rbx * INDICE_OFFSET + 2]
	MOV rdi, [r12+r8*8]
	MOV rsi, [r12+r9*8]

	call r15

	CMP al, 0
	JE .noIgual

	INC rbx
	CMP rbx, r14
	JE .fin
	JMP .loop

	.fin:
	MOV rax, 1
	ADD rsp, 8
	POP rbx
	POP r15
	POP r14
	POP r13
	POP r12
	POP rbp
	ret 

	.noIgual:
	MOV rax, 0
	ADD rsp, 8
	POP rbx
	POP r15
	POP r14
	POP r13
	POP r12
	POP rbp
	ret









;; Dado un inventario y una vista, crear un nuevo inventario que mantenga el
;; orden descrito por la misma.

;; La memoria a solicitar para el nuevo inventario debe poder ser liberada
;; utilizando `free(ptr)`.

;; item_t** indice_a_inventario(item_t** inventario, uint16_t* indice, uint16_t tamanio);

;; Donde:
;; - `inventario` un array de punteros a ítems que representa el inventario a
;;   procesar.
;; - `indice` es el arreglo de índices en el inventario que representa la vista
;;   que vamos a usar para reorganizar el inventario.
;; - `tamanio` es el tamaño del inventario.
;; 
;; Tenga en consideración:
;; - Tanto los elementos de `inventario` como los del resultado son punteros a
;;   `ítems`. Se pide *copiar* estos punteros, **no se deben crear ni clonar
;;   ítems**
PUNTERO_OFFSET EQU 8
global indice_a_inventario
indice_a_inventario:
	; Te recomendamos llenar una tablita acá con cada parámetro y su
	; ubicación según la convención de llamada. Prestá atención a qué
	; valores son de 64 bits y qué valores son de 32 bits o 8 bits.
	;
	; r/m64 = item_t**  inventario
	; r/m64 = uint16_t* indice
	; r/m16 = uint16_t  tamanio
	;
	;ITEM_t SIZE OF = 18 ( 2) + 4+ 2 (2) = 28
	PUSH rbp
	MOV rbp, rsp
	PUSH r12
	PUSH r13
	PUSH r14
	PUSH rbx

	MOV r12, rdi
	MOV r13, rsi
	MOVZX r14, edx

	MOV rdi, 8
	IMUL rdi, r14

	CALL malloc

	XOR rcx, rcx
	MOV rbx, rax

	.loop:

	MOVZX r8, word  [r13 + rcx*INDICE_OFFSET]
	MOV r9, [r12 + r8*PUNTERO_OFFSET]
	MOV [rbx + rcx*PUNTERO_OFFSET], r9

	INC rcx
	CMP rcx, r14
	JE .fin
	JMP .loop


	.fin:
	POP rbx
	POP r14
	POP r13
	POP r12
	POP rbp
	ret
