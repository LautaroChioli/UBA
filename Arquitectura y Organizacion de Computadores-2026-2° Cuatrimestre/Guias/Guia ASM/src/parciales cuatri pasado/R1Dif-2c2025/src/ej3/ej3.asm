;########### SECCION DE DATOS
section .data

;########### SECCION DE TEXTO (PROGRAMA)
section .text

; Completar las definiciones (serán revisadas por ABI enforcer):
ITEM_KIND_OFFSET EQU 0
ITEM_WEIGHT_OFFSET EQU 4
ITEM_SIZE EQU 8

BACKPACK_ITEMS_OFFSET EQU 0
BACKPACK_MAX_WEIGHT_OFFSET EQU 8
BACKPACK_ITEM_COUNT_OFFSET EQU 12
BACKPACK_SIZE EQU 16

DESTINATION_NAME_OFFSET EQU 0
DESTINATION_REQUIREMENTS_OFFSET EQU 32
DESTINATION_REQUIREMENTS_SIZE_OFFSET EQU 40
DESTINATION_SIZE EQU 48

EVENT_NEXT_OFFSET EQU 0
EVENT_DESTINATION_OFFSET EQU 8
EVENT_SIZE EQU 16

ITINERARY_FIRST_OFFSET EQU 0
ITINERARY_SIZE EQU 8


NULL EQU 0

extern backpackContainsItem
extern malloc
extern free 
extern calloc

; backpack_t *prepareBackpack(itinerary_t *itinerary, uint8_t getItemWeight(item_kind_t))
; backpack_t *prepareBackpack(itinerary_t *itinerary, uint8_t getItemWeight(item_kind_t))
global prepareBackpack 
prepareBackpack:

    PUSH rbp
    MOV rbp, rsp
    PUSH r12
    PUSH r13
    PUSH r14
    PUSH r15
    PUSH rbx
    SUB rsp, 8          ; Alineamos la pila a 16 bytes

    MOV r15, rdi        ; r15 = puntero a itinerario
    MOV r14, rsi        ; r14 = puntero a la funcion getItemWeight
    MOV r13, [r15 + ITINERARY_FIRST_OFFSET] ; r13 = evento actual
    
    CMP r13, 0
    JE .ItinerarioVacio

    ; 1. Creo la lista de totales (7 items x 4 bytes c/u) iniciada en ceros
    MOV rdi, 7
    MOV rsi, 4
    CALL calloc
    MOV r12, rax        ; r12 = puntero a mi lista de totales
    
.loopEventos:
    CMP r13, 0
    JE .finEventos

    MOV r8, [r13 + EVENT_DESTINATION_OFFSET] ; r8 = destino
    MOV r9, [r8 + DESTINATION_REQUIREMENTS_OFFSET] ; r9 = lista de requerimientos
    MOVZX r10, dword [r8 + DESTINATION_REQUIREMENTS_SIZE_OFFSET] ; r10 = cant. requerimientos
    XOR rcx, rcx        ; rcx = contador de requerimientos

.loopRequisitos:
    CMP rcx, r10 
    JE .siguienteEvento

    MOV edx, dword [r9 + rcx*4] ; edx = item requerido (leo 4 bytes)
    INC dword [r12 + rdx*4]     ; sumo 1 al contador de ese item

    INC rcx
    JMP .loopRequisitos

.siguienteEvento:
    MOV r13, [r13 + EVENT_NEXT_OFFSET] ; Avanzo al siguiente evento
    JMP .loopEventos

.finEventos:
    ; 2. Cuento cuántos items DISTINTOS necesito y cuánta memoria ocupan
    XOR rcx, rcx        ; iterador (0 a 6)
    XOR rbx, rbx        ; rbx = tamaño en bytes que voy a pedir (arranca en 0)

.cuentoBytes:
    CMP rcx, 7
    JE .pedirMemoriaItems
    
    CMP dword [r12 + rcx*4], 0  ; ¿Necesito este item?
    JE .noAparece
    ADD rbx, ITEM_SIZE          ; Si lo necesito, sumo 8 bytes
.noAparece:
    INC rcx
    JMP .cuentoBytes

.pedirMemoriaItems:
    MOV rdi, rbx
    CALL malloc
    MOV r15, rax        ; r15 = array final de items

    ; 3. Lleno el array de items preguntando los pesos
    XOR r13, r13        ; r13 = kind del item (de 0 a 6). Uso r13 para no perderlo en el CALL.
    XOR rbx, rbx        ; rbx = cantidad de items guardados (índice)

.veoCualesItemsEstan:
    CMP r13, 7
    JE .listaTerminada

    CMP dword [r12 + r13*4], 0  ; Si es 0, no lo necesito
    JE .saltarItem

    ; Pido el peso
    MOV rdi, r13        ; rdi = kind actual
    CALL r14            ; llamo a getItemWeight(kind). El peso vuelve en 'al'

    ; Guardo los datos en el array
    MOV dword [r15 + rbx*ITEM_SIZE + ITEM_KIND_OFFSET], r13d ; Guardo el kind (4 bytes)
    MOV byte  [r15 + rbx*ITEM_SIZE + ITEM_WEIGHT_OFFSET], al ; Guardo el peso (1 byte)

    INC rbx             ; Aumento la cantidad de items guardados

.saltarItem:
    INC r13
    JMP .veoCualesItemsEstan

.listaTerminada:
    ; Ya no necesito la lista de totales (r12)
    MOV rdi, r12
    CALL free

    ; 4. Creo la mochila
    MOV rdi, BACKPACK_SIZE
    CALL malloc
    
    ; 5. Guardo los datos en la mochila
    MOV qword [rax + BACKPACK_ITEMS_OFFSET], r15     ; Puntero al array de items
    MOV byte  [rax + BACKPACK_MAX_WEIGHT_OFFSET], 255 ; Peso máximo
    MOV dword [rax + BACKPACK_ITEM_COUNT_OFFSET], ebx ; Cantidad final de items (ebx es 32 bits)

    ADD rsp, 8
    POP rbx
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp
    ret

.ItinerarioVacio:
    MOV rdi, BACKPACK_SIZE
    CALL malloc
    
    ; Lo relleno bien con ceros para no dejar basura
    MOV qword [rax + BACKPACK_ITEMS_OFFSET], 0      ; Puntero a NULL
    MOV byte  [rax + BACKPACK_MAX_WEIGHT_OFFSET], 255
    MOV dword [rax + BACKPACK_ITEM_COUNT_OFFSET], 0 ; 0 items

    ADD rsp, 8
    POP rbx
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp
    ret