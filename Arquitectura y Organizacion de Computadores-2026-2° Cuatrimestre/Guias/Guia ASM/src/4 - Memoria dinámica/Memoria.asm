extern malloc
extern free
extern fprintf

section .data

section .text

global strCmp
global strClone
global strDelete
global strPrint
global strLen

; ** String **

; int32_t strCmp(char* a, char* b)
strCmp:
.loop:
    mov al, byte [rdi]    ; Load character from string 'a'
    cmp al, byte [rsi]    ; Compare it to character from string 'b'
    jne .areNotEqual      ; If they don't match, return 0

    cmp al, 0             ; Did we just successfully match the null terminator?
    je .areEqual          ; If yes, we reached the end of both strings safely

    inc rdi               ; Move to the next character in 'a'
    inc rsi               ; Move to the next character in 'b'
    jmp .loop             ; Repeat for the next character

.areNotEqual:
    mov rax, 0
    ret

.areEqual:
    mov rax, 1
    ret



; char* strClone(char* a)
; Input: rdi (pointer to string 'a')
; Output: rax (pointer to new cloned string)
strClone:
    ; 1. Prologue: Save callee-saved register and align stack
    ; Pushing 8 bytes (rbx) + the 8-byte return address = 16-byte aligned stack.
    push rbx
    
    ; Handle NULL pointer just in case
    test rdi, rdi
    jz .ret_null

    mov rbx, rdi          ; Save the original string pointer safely in rbx

    ; 2. Calculate Length
    xor rcx, rcx          ; rcx = 0 (length counter)
.len_loop:
    cmp byte [rbx + rcx], 0
    jz .len_done
    inc rcx
    jmp .len_loop

.len_done:
    ; 3. Allocate Memory
    mov rdi, rcx
    inc rdi               ; rdi = length + 1 (for the null terminator)
    call malloc		  ; malloc agarra rdi para saber cuantos bytes guardar, y lo devuelve en rax
    
    ; Check if malloc returned NULL
    test rax, rax
    jz .cleanup

    ; 4. Copy the String
    ; rbx = source pointer, rax = destination pointer
    xor rcx, rcx          ; Reset index counter to 0
.copy_loop:
    mov dl, byte [rbx + rcx]   ; Read 1 byte (char) into 8-bit register dl
    mov byte [rax + rcx], dl   ; Write 1 byte to the new memory
    
    inc rcx                    ; Move to the next character
    
    test dl, dl                ; Did we just copy the 0 (null terminator)?
    jnz .copy_loop             ; If not 0, keep looping

    ; Note: Because we use [rax + rcx], rax itself is never modified!
    ; It still points to the start of the string, exactly as required for the return.

.cleanup:
    ; Epilogue: Restore the register and return
    pop rbx
    ret

.ret_null:
    xor rax, rax          ; Return NULL if input was NULL
    pop rbx
    ret



; void strDelete(char* a)
strDelete:
	CMP byte [edi], 0
	JZ .fin

	.loop:
	MOV byte [edi], 0
	INC edi
	CMP byte [edi], 0
	JZ .fin
	JMP .loop

	.fin:
	ret


; void strPrint(char* a, FILE* pFile) syscall write: RAX=1(call number for write), RDI=1(stdout), RSI=memory address of first char, RDX = length of string
strPrint:
	XOR rax,rax
	MOV r8, rdi
	MOV rdi, 1
	MOV rax, 1
	
	MOV r9, r8
	CMP byte [r9], 0
	JZ .print

	.count:
	INC r9
	CMP byte [r9], 0
	JZ .print
	JMP .count

	.print:
	MOV rsi, r8
	SUB r9, r8
	MOV rdx, r9
	syscall
	ret



; uint32_t strLen(char* a)
strLen:
	XOR rax, rax
	XOR rcx, rcx
	.loop:
	CMP byte [rdi], 0
	JZ .fin
	INC rcx
	ADD rdi, 1
	JMP .loop

	.fin:
	MOV rax, rcx
	ret


