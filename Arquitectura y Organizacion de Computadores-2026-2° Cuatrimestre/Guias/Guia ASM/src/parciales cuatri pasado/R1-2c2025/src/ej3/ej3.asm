extern malloc


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
REC_SIZE                   EQU 16   ; sizeof(Recorrido)


; Notar que el enum aparece como puntero, entonces no afecta los offsets
; uint32_t sumarTesoros(Mapa *mapa, uint32_t actual, bool *visitado);

global sumarTesoros
sumarTesoros:
    ; --- 1. PRÓLOGO Y BÚNKER ---
    PUSH rbp
    MOV rbp, rsp
    PUSH r12
    PUSH r13
    PUSH r14
    PUSH r15
    PUSH rbx
    SUB rsp, 8


    MOV r13, rdi            ; r13 = mapa 
    MOV ebx, esi            ; rbx = ID actual 
    MOV r14, rdx            ; r14 = visitado 
    XOR r12, r12            ; r12 = acumulador 

    CMP byte [r14 + rbx], 0 ; cheequeo si ya lo visite
    JNE .volver

    MOV byte [r14 + rbx], 1 ; si no estive marco que visite

    MOV r15, [r13 + MAP_HABITACIONES_OFFSET] ; puntero a las habitaciones
    MOV rax, rbx
    IMUL rax, HAB_SIZE
    ADD r15, rax            ; r15 = habitacion actual

    CMP byte [r15 + HAB_CONTENIDO_OFFSET + CONT_ES_TESORO_OFFSET], 0
    JE .vecino0             ; si no ahy oro sigo de largo

    ; si hay, sumo al total
    MOV eax, dword [r15 + HAB_CONTENIDO_OFFSET + CONT_VALOR_OFFSET]
    ADD r12, rax

.vecino0:
    MOV edi, dword [r15 + HAB_VECINOS_OFFSET]       ; leo al norte
    CMP edi, 99
    JE .vecino1
    
    MOV rsi, rdi            ; rsi = ID del vecino
    MOV rdi, r13            ; rdi = mapa
    MOV rdx, r14            ; rdx = visitado
    CALL sumarTesoros
    ADD r12, rax            ; sumo al total lo del vecino

.vecino1:
    MOV edi, dword [r15 + HAB_VECINOS_OFFSET + 4]   ; leo al sur
    CMP edi, 99
    JE .vecino2
    MOV rsi, rdi
    MOV rdi, r13
    MOV rdx, r14
    CALL sumarTesoros
    ADD r12, rax

.vecino2:
    MOV edi, dword [r15 + HAB_VECINOS_OFFSET + 8]   ; leo al este
    CMP edi, 99
    JE .vecino3
    MOV rsi, rdi
    MOV rdi, r13
    MOV rdx, r14
    CALL sumarTesoros
    ADD r12, rax

.vecino3:
    MOV edi, dword [r15 + HAB_VECINOS_OFFSET + 12]  ; leo aal oseste
    CMP edi, 99
    JE .fin
    MOV rsi, rdi
    MOV rdi, r13
    MOV rdx, r14
    CALL sumarTesoros
    ADD r12, rax

.fin:
    MOV rax, r12            ; Guardo todo el oro acumulado para devolverlo
    ADD rsp, 8
    POP rbx
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp
    ret

.volver:
    XOR rax, rax            ; Devuelvo 0
    ADD rsp, 8
    POP rbx
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp
    ret
 


    
