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
extern free

; void filterPossibleDestinations(itinerary_t *itinerary, backpack_t *backpack)
global filterPossibleDestinations
filterPossibleDestinations:

    PUSH rbp,
    MOV rbp, rsp
    PUSH r12
    PUSH r13
    PUSH r14    
    PUSH r15 
    PUSH rbx
    SUB rsp, 8

    MOV r15, rdi  ; r15 = *itinerario
    MOV r14, rsi ; r14 = *backpack
    MOV r13, [r14 + BACKPACK_ITEMS_OFFSET] ; r13 = items
    MOV r12, [r15 + ITINERARY_FIRST_OFFSET] ; r12 = evento actual
    XOR rbx, rbx ;guardo en rbx el puntero anterior 

    CMP [r15], 0
    JE .sinItinerario

    .loop:
    MOV r8, [r12 + EVENT_DESTINATION_OFFSET] ;encuentro destino actual
    MOV rdi, r14  ; copio *backpack a rdi
    MOV rsi, r8   ;copio el destino a rsi

    call meetsRequirements ; devuelve 0 si hay un item que necesite y no tenga

    CMP rax, 0
    JE .noTengoItemNecesario

    MOV r9, r12  ; guardo en r9 el actual
    MOV r8, [r12 + EVENT_NEXT_OFFSET] ; r8 = next
    MOV r12, r8 ; actualizo evento actual a ex next
    MOV rbx, r9 ; rbx ahora es ex actual, ahora anteriro

    CMP r12, 0
    JE .noMasLista

    JMP .loop

    .noTengoItemNecesario:

    MOV rdi, r12  ; guardo en rdi el evento actual
    MOV r8, [r12] ; guardo en r8 el next
    CMP rbx, 0
    JE .primerCaso

    MOV [rbx], r8 ; el anterior ahora apunta aal next
    MOV r12, r8 ; el next a hora es el actual

    call freeEvent

    CMP r12, 0
    JE .noMasLista
    JMP .loop

    .primerCaso:

    MOV [r15], r8
    MOV r12, r8

    call freeEvent

    CMP r12, 0
    JE .noMasLista
    JMP .loop

    .noMasLista:

    ADD rsp, 8
    POP rbx
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp
    ret

    .sinItinerario:
    
    ADD rsp, 8
    POP rbx
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp
    ret


;meetsRequirements(backpack_t *backpack, destination_t *dest)`

meetsRequirements:

    ;rdi = *backpack
    ;rsi = *destination

    PUSH rbp,
    MOV rbp, rsp
    PUSH r12
    PUSH r13
    PUSH r14
    PUSH r15
    PUSH rbx
    SUB rsp, 8


    XOR rcx, rcx ; uso rcx como contador de items requeridos
    XOR r12, r12 ; uso r12 como contador de items en mochila

    MOV r8, [rsi + DESTINATION_REQUIREMENTS_OFFSET] ; r8 = puntero a requerimientos
    MOVZX r9, dword [rsi + DESTINATION_REQUIREMENTS_SIZE_OFFSET] ; r9 = cantidad de reqieromientos

    CMP r9, 0
    JE .noMasRequeridos

    MOV r10, [rdi + BACKPACK_ITEMS_OFFSET] ; r10 = puntero a items en mochila
    MOVZX r11, dword [rdi + BACKPACK_ITEM_COUNT_OFFSET] ; r11 = cantidad de items en mochila

    CMP r11, 0
    JE .noEstaElItemEnLaMochila

    .encuentroRequerido:

    MOVZX rdx, dword [r8 + rcx*4] ; rdx = item requerido

    .buscoItemEnMochila:

    MOVZX rax, dword [r10 + r12 * ITEM_SIZE] 

    CMP rdx, rax
    JE .itemRequeridoEncontrado

    INC r12
    CMP r12, r11
    JE .noEstaElItemEnLaMochila

    JMP .buscoItemEnMochila


    .itemRequeridoEncontrado:

    INC rcx
    CMP rcx, r9
    JE .noMasRequeridos
    JMP .encuentroRequerido


    .noMasRequeridos:
    XOR rcx, rcx
    MOV rax, 1

    ADD rsp, 8
    POP rbx
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp

    ret

    .noEstaElItemEnLaMochila:
    XOR rcx, rcx
    XOR rax, rax

    ADD rsp, 8
    POP rbx
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp
    ret


; `free_event(event_t *event)` 
freeEvent:

    PUSH rbp
    MOV rbp, rsp
    PUSH r12
    PUSH r13
    PUSH r14
    PUSH r15
    PUSH rbx
    SUB rsp, 8
    ; rdi = *event
    MOV r12, rdi ; r12 = *event

    

    mov r13, [r12 + EVENT_DESTINATION_OFFSET]

    mov rdi, [r13 + DESTINATION_REQUIREMENTS_OFFSET]        ; al llamar a free, solo se borran los punteros

    call free

    mov rdi, r13

    call free



    mov rdi, r12

    call free 

    ADD rsp, 8
    POP rbx
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp
    ret


