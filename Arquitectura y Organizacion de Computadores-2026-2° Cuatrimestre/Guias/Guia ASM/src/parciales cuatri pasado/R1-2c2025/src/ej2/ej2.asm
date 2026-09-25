; ------------------------
; Offsets para los structs
; Plataforma: x86_64 (LP64)
; ------------------------
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


; Recorrido *invertirRecorridoConDirecciones(const Recorrido *rec, uint64_t len);
global  invertirRecorridoConDirecciones
invertirRecorridoConDirecciones:

    PUSH rbp
    MOV rbp, rsp
    PUSH r12
    PUSH r13
    PUSH r14
    PUSH r15
    PUSH rbx
    SUB rsp, 8

    MOV r12, rdi ;recorrido* en r12
    MOV r13, rsi ; distancia en r13

    

    MOV rdi, r13
    IMUL rdi, 4   ; calculo tamaño de malloc

    CMP r12, 0
    JE .NoHayRecorrido
    
    CMP r13, 0
    JE .NoHayRecorrido

    CALL malloc ; creo nuevo array tamaño recorrido

    MOV R14, RAX ; guardo en r14 el puntero al nuevo recorrido
    XOR r15, r15 ; uso r15 como contador
    CMP r12, 0
    JE .NoHayRecorrido

    MOV rbx, [r12 + REC_ACCIONES_OFFSET]; guardo en rbx puntero a acciones

    CMP r13, 0
    JE .NoHayRecorrido
    MOV r10, r13 
    DEC r10

    XOR rdi, rdi
    .loop:
    MOV edi, dword [rbx +  r10*4] ; pongo en rdi el movimiento actual
    PUSH r10
    SUB rsp, 8

    call invertirDireccion

    ADD rsp, 8
    POP r10
    MOV dword [r14 + r15*4], eax ; pongo direccion contraria en nuevo array


    INC r15
    DEC r10
    CMP r15, r13
    JE .noMasAcciones

  
    JMP .loop

    .noMasAcciones:
    
    MOV rdi, 16 ; tamaño de recorrido
    
    CALL malloc

    mov [rax + REC_ACCIONES_OFFSET], r14
    MOV [rax + REC_CANT_ACCIONES_OFFSET], r13

    ADD rsp, 8
    POP rbx
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp
    ret

    .NoHayRecorrido:
    XOR rax, rax
    ADD rsp, 8
    POP rbx
    POP r15
    POP r14
    POP r13
    POP r12
    POP rbp
    ret














invertirDireccion:

    CMP rdi, 0
    JE .EntraNorteDevolverSur

    CMP rdi, 1
    JE .EntraSurDevolverNorte

    CMP rdi, 2
    JE .EntraEsteDevolverOeste

    CMP rdi, 3
    JE .EntraOesteDevolverOeste




    .EntraNorteDevolverSur:
    
    MOV rax, 1
    ret

    .EntraSurDevolverNorte:

    MOV rax, 0
    ret

    .EntraEsteDevolverOeste:
    MOV rax, 3
    ret

    .EntraOesteDevolverOeste:
    MOV rax, 2
    ret
    
