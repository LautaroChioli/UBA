;########### SECCION DE DATOS
section .data

;########### SECCION DE TEXTO (PROGRAMA)
section .text

; Completar las definiciones (serán revisadas por ABI enforcer):
;ITEM_T
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

; bool canItemFitInBackpack(backpack_t *backpack, item_t *item)
global canItemFitInBackpack
canItemFitInBackpack:

    PUSH rbp,
    MOV rbp, rsp
    PUSH r12
    PUSH r13
    PUSH r14    ;r12 = backapck*
    PUSH r15    ;r13 = item_t*


    MOV r12, rdi
    MOV r13, rsi
    XOR rcx, rcx


    MOV rdi, [r12 + BACKPACK_ITEMS_OFFSET] ; rdi = items en mochila
    MOVZX rsi, dword [r12 + BACKPACK_ITEM_COUNT_OFFSET] ; rsi= cuantos items hay en la mochila
    MOVZX rdx, byte [r12 + BACKPACK_MAX_WEIGHT_OFFSET];rdx = peso maaximo

    XOR rax, rax ; acumulador de peso total
    XOR r8, r8

    CMP rdi, 0 ;CASO MOCHILA VACIA
    JE .mochilaVacia




    .calcularPesoMochila:
    MOV r11, rdi
    ADD r11, ITEM_WEIGHT_OFFSET
    MOVZX r8, byte [r11 + rcx*ITEM_SIZE] ; r8 = peso del item

    ADD rax, r8 ; sumo peso de item actual al total

    INC rcx
    CMP rcx, rsi
    JE .noMasItemsEnMochila

    
    JMP .calcularPesoMochila



    .noMasItemsEnMochila:

    MOV r8, rax ; guardo en r8 el peso total de la mochila
    MOVZX r9, byte [r13 + ITEM_WEIGHT_OFFSET] ; guardo en r9 el peso del item que quiero guardar
    ADD r8, r9 ; r8 = peso viejo + nuevo item
    CMP rdx, r8
    JAE .entraElItem
    JMP .noEntraElITem

    .entraElItem:
    MOV rax, 1
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp
    ret


    .noEntraElITem:
    MOV rax, 0
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp
    ret

    
    .mochilaVacia:

    MOVZX r9, byte [r13 + ITEM_WEIGHT_OFFSET] ;guardo en r9 el peso del item que quiero guardar
    MOVZX r10, byte [r12 + BACKPACK_MAX_WEIGHT_OFFSET]

    CMP r9, r10
    JA .noEntraElITem
    JMP .entraElItem
    