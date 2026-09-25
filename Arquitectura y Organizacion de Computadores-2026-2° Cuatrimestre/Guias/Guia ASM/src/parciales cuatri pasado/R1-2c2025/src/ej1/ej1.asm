; ------------------------
; Offsets para los structs
; Plataforma: x86_64 (LP64)
; ------------------------

section .data

section .text

; COMPLETAR las definiciones (serán revisadas por ABI enforcer):
; ------------------------
; Contenido
; ------------------------
CONT_NOMBRE_OFFSET      EQU 0        ; char nombre[64]
CONT_VALOR_OFFSET       EQU 64        ; uint32_t valor
CONT_COLOR_OFFSET       EQU 68       ; char color[32]
CONT_ES_TESORO_OFFSET   EQU 100      ; bool es_tesoro ;;;;;;;;;;;;;;;;;;;;;;;;;;;;BOOL = 1 BYTE ACORDATE DEL PADDING, FLOAT = 4 BYTES
CONT_PESO_OFFSET        EQU 104      ; float peso
CONT_SIZE               EQU 108      ; sizeof(Contenido) (rounded)

; ------------------------
; Habitacion
; ------------------------
HAB_ID_OFFSET          EQU 0        ; uint32_t id
HAB_VECINOS_OFFSET     EQU 4        ; uint32_t vecinos[ACC_CANT]
HAB_CONTENIDO_OFFSET   EQU 20        ; Contenido contenido
HAB_VISITAS_OFFSET     EQU 128       ; uint32_t visitas
HAB_SIZE               EQU 132       ; sizeof(Habitacion)

; ------------------------
; Mapa
; ------------------------
MAP_HABITACIONES_OFFSET    EQU 0     ; Habitacion *habitaciones
MAP_N_HABITACIONES_OFFSET  EQU 8      ; uint64_t n_habitaciones
MAP_ID_ENTRADA_OFFSET      EQU 16      ; uint32_t id_entrada
MAP_SIZE                   EQU 24    ; sizeof(Mapa)

; ------------------------
; Recorrido
; ------------------------
REC_ACCIONES_OFFSET        EQU 0     ; Accion *acciones
REC_CANT_ACCIONES_OFFSET   EQU 8     ; uint64_t cant_acciones
REC_SIZE                   EQU 16     ; sizeof(Recorrido)

; Notar que el enum aparece como puntero, entonces no afecta los offsets
; bool encontrarTesoroEnMapa(Mapa *mapa, Recorrido *rec, uint64_t *acciones_ejecutadas)
global  encontrarTesoroEnMapa
encontrarTesoroEnMapa:

    PUSH rbp
    MOV rbp, rsp
    PUSH r12
    PUSH r13
    PUSH r14
    PUSH r15
    PUSH rbx
    SUB rsp, 8

    MOV r12, rdi ;r12 = *mapa
    MOV r13, rsi ;r13 = *recorrido
    MOV r14, rdx ;r14 = *acc_ejecutadas

    MOV r9d, dword [r12 + MAP_ID_ENTRADA_OFFSET] ;guardo en r9 el indice de la habitacion de entarada
    MOV r8, [r12 + MAP_HABITACIONES_OFFSET] ;guardo en r8 el puntero a las habitaciones
    IMUL r9, HAB_SIZE
    MOV rdi, r8
    ADD rdi, r9 ; rdi es puntero a habitacion
    MOV r10, [r13 + REC_CANT_ACCIONES_OFFSET] ; guardo en r10 cuantas acciones hay en total
    XOR rcx, rcx ; seteo rcx en 0, para usar de contador
    MOV rbx, [r13 + REC_ACCIONES_OFFSET]

    .loop:

    MOVZX r11,byte  [rdi + HAB_CONTENIDO_OFFSET + CONT_ES_TESORO_OFFSET] ; guardo en r11 si hay tesoro
    ;MOV rsi, [r11 + CONT_ES_TESORO_OFFSET] ; guardo en rsi si hay tesoro

    CMP r11, 0
    JNE .hayTesoro


    MOVZX rsi, word [rbx + rcx*4] ;accedo a la i-esima accion
    MOVZX r15, word dword [rdi + HAB_VECINOS_OFFSET + rsi*4] ; guardo en r15 la id de la siguiente habitacion
    

    CMP r15, 99
    JE .NoHayVecino

    imul r15, HAB_SIZE
    MOV rdi, r8
    ADD rdi, r15
    

    CMP rcx, r10
    JE .noMasAcciones

    INC rcx
    INC [r14]
    JMP .loop

    .hayTesoro:
    MOV rax, 1
    ADD rsp, 8
    POP rbx
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp
    ret

    .NoHayVecino:
    XOR rax, rax
    ADD rsp, 8
    POP rbx
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp
    ret 
    .noMasAcciones:
    xor rax, rax
    ADD rsp, 8
    POP rbx
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp

    ret