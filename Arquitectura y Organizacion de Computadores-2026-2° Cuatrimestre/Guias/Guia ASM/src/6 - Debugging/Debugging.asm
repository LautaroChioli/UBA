extern strcpy
extern malloc
extern free

section .rodata
; Acá se pueden poner todas las máscaras y datos que necesiten para el ejercicio

section .text
; Marca un ejercicio como aún no completado (esto hace que no corran sus tests)
FALSE EQU 0
; Marca un ejercicio como hecho
TRUE  EQU 1

ITEM_OFFSET_ID EQU 12
ITEM_OFFSET_CANTIDAD EQU 16

POINTER_SIZE EQU 8
UINT32_SIZE EQU 4

; Marcar el ejercicio como hecho (`true`) o pendiente (`false`).

global EJERCICIO_1_HECHO
EJERCICIO_1_HECHO: db FALSE ; Cambiar por `TRUE` para correr los tests.

global EJERCICIO_2_HECHO
EJERCICIO_2_HECHO: db FALSE ; Cambiar por `TRUE` para correr los tests.

global EJERCICIO_3_HECHO
EJERCICIO_3_HECHO: db FALSE ; Cambiar por `TRUE` para correr los tests.

global EJERCICIO_4_HECHO
EJERCICIO_4_HECHO: db TRUE ; Cambiar por `TRUE` para correr los tests.

global ejercicio1
ejercicio1:
	add rdi, rsi
    add rdi, rdx
    add rdi, rcx
	add rdi, r8
	mov rax, rdi
	ret

global ejercicio2
ejercicio2:		;		rdi = puntero a nuevo struct, rsi= id, rdx = cantidada, rcx= nombre (string)
	mov [rdi+ITEM_OFFSET_ID], esi
	mov [rdi+ITEM_OFFSET_CANTIDAD], rdx
	mov rsi, rcx
	call strcpy
	ret


global ejercicio3
ejercicio3:
	cmp rsi, 0
	je .vacio
	
	mov rcx, rdi ; array
	mov r11, rsi ; n
	mov r8, 0 ; sumatoria
	mov r9, 0 ; i

	
	.loop:    
	mov rdi, r8
	mov rsi, [rcx + r9*4]

	call rdx

	add r8, rax
	mov rax, r8

	inc r9

	mov rsi, r11
	cmp r9, rsi
	je .end

	jmp .loop

	.vacio:
	mov rax, 64

	.end:
	ret

; POINTER_SIZE EQU 8
; UINT32_SIZE EQU 4
global ejercicio4
ejercicio4:
	push rbp
    mov rbp, rsp
    push r12
    push r13
    push r14
    push r15
    push rbx
	sub rsp, 8	
	mov r12, rdi
	mov r13, rsi
	mov r14, rdx

	xor rdi, rdi
	mov rdi, UINT32_SIZE
	imul edi, esi
	mov edi, eax

	call malloc  ; CUANDO LLAMO MALLOC EN RDI VAN CUANTOS BYTES!!!, DEVUELVE EN RAX, COMO TODAS LAS FUNCIONES
	mov r15, rax
	
	xor rbx, rbx
	.loop:
	
	cmp rbx, r13
	je .end

	mov r8, [r12+rbx*POINTER_SIZE]
	mov r9d, [r8]
	mov eax, r14d
	imul eax, r9d
	mov [r15+rbx*UINT32_SIZE], eax
	
	mov rdi, r8
	call free

	mov qword [r12+rbx*POINTER_SIZE], 0

	inc rbx
	jmp .loop

	.end:
	mov rax, r15
	add rsp, 8
    pop rbx
    pop r15
    pop r14
    pop r13
    pop r12
    pop rbp
	ret
