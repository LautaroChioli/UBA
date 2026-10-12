; Hace que los accesos a memoria por defecto se compilen como [rip + offset]
; en lugar de [offset_desde_el_0x0].
;
; Ver https://www.nasm.us/doc/nasmdoc7.html#section-7.2.1 para más información
DEFAULT REL

TRUE  EQU 1
FALSE EQU 0

SINCOS_SIN_OFF EQU 0
SINCOS_COS_OFF EQU 4
SINCOS_SZ      EQU 8

section .rodata


ALIGN 16
espacios:
	times 10 db ' ' - '0'
	times 6  db 0x0
ceros:
	times 10 db '0'
	times 6  db 0x0


section .text

global ej1_sample
; void ej1_sample(size_t buf_len, int16_t buf[buf_len],
;                 size_t freq_a_len, int16_t freq_a[freq_a_len], size_t a_start,
;                 size_t freq_b_len, int16_t freq_b[freq_b_len], size_t b_start);

ej1_sample:		;		rdi = buf_len, rsi = buf, rdx = a_len, rcx = freq_a, r8 = a_start, r9 = b_len, [rsp+8] = freq_b, [rsp+16] = b_start

	push rbx	; push a la pila
	push rbp
	push r12
	push r13
	push r14
	push r15		

	mov  r12, rdi	; pongo en r12 las  muestras restantes por escribir
	mov  r13, rdx	; r13 = a_len
	mov  r14, rcx	; r14 = freq_a
	mov  r15, r9	; r15 = b_len
	mov  rbx, [rsp + 56]	; rbx = freq_b
	mov  rbp, [rsp + 64]	; rbp = b_start

	mov  rax, r8
	xor  edx, edx	; seteo a 0 la parte alta para dividir
	div  r13	; rdx = a_start mod a_len
	mov  r8, rdx	; r8 = indice a

	mov  rax, rbp
	xor  edx, edx
	div  r15
	mov  rbp, rdx			; rbp = indice b

.loop:
	test r12, r12	
	jz   .epilogo


	mov  r10, r13
	sub  r10, r8			; r10 = a_len - indice a 
	mov  r11, r15
	sub  r11, rbp			; r11 = b_len - indice b
	cmp  r11, r10
	cmovb r10, r11
	cmp  r12, r10
	cmovb r10, r12			; r10 = n
	sub  r12, r10			; restante -= n

	lea  rax, [r14 + r8*2]		; rax = direccion de freq_a[ia]
	lea  rdx, [rbx + rbp*2]		
	mov  r9, r10			

.suma8:					
	movdqu xmm0, [rax]		; agarro 8 instantes de A
	movdqu xmm1, [rdx]		; mismo para B
	paddw  xmm0, xmm1		; A + B
	movdqa xmm2, xmm0
	psrlw  xmm2, 15			
	paddw  xmm0, xmm2		
	psraw  xmm0, 1			; suma / 2
	movdqu [rsi], xmm0
	add  rax, 16
	add  rdx, 16
	add  rsi, 16
	sub  r9, 8
	jnz  .suma8

	add  r8, r10			; indice a += n
	add  rbp, r10			; indice b += n
	cmp  r8, r13		
	jne  .checkb
	xor  r8, r8
.checkb:
	cmp  rbp, r15
	jne  .loop
	xor  ebp, ebp
	jmp  .loop

.epilogo:
	pop  r15
	pop  r14
	pop  r13
	pop  r12
	pop  rbp
	pop  rbx
	ret

	
global ej2_detect
; float ej2_detect(size_t size, int16_t signal[size], sincos_t freq[size]);
;
ej2_detect:
	xorps xmm4, xmm4	; pongo en xmm4 los reales, 4 por xmm
	xorps xmm5, xmm5	; mismo para xmm5
	mov   rcx, rdi		; rcx = muestras restantes

.loop:
	pmovsxwd xmm0, [rsi]	 ; para pasar a float se neciesitan int32, los paso agregando padding
	cvtdq2ps xmm0, xmm0		 ; convierto a float
	movups xmm1, [rdx]		 ; [sin0, cos0, sin1, cos1]
	movups xmm2, [rdx + 16]	 ; [sin2, cos2, sin3, cos3]
	movaps xmm3, xmm1
	shufps xmm1, xmm2, 0x88	 ; xmm1 = [sin0, sin1, sin2, sin3]
	shufps xmm3, xmm2, 0xDD	 ; xmm3 = [cos0, cos1, cos2, cos3]
	mulps  xmm1, xmm0		 ; voy multiplicando las 4 señales por los senos
	mulps  xmm3, xmm0	     ; tambien por los cosenos
	addps  xmm5, xmm1		 ; le sumo el resultado en xmm1 a los imaginarios
	addps  xmm4, xmm3	     ; y en xmm3 a los reales
	add  rsi, 8
	add  rdx, 32
	sub  rcx, 4				 ; paso a las siguientes 4 señales
	jnz  .loop

	haddps xmm4, xmm4   ; sumo todos los reales
	haddps xmm4, xmm4	; xmm4[0] = re
	haddps xmm5, xmm5	; sumo los imaginarios
	haddps xmm5, xmm5	; xmm5[0] = im

	mulss  xmm4, xmm4   ; re^2 
	mulss  xmm5, xmm5	; im^2
	addss  xmm4, xmm5	; re^2 + im^2
	sqrtss xmm0, xmm4 	; xmm0 = sqrt(re^2 + im^2)
	addss  xmm0, xmm0	; * 2
	cvtsi2ss xmm1, rdi  ; paso a float para poder hacer la division
	divss  xmm0, xmm1	; / size
	ret

global ej3_remove_duplicates
; void ej3_remove_duplicates(size_t size, char detected[size], char output[]);

ej3_remove_duplicates:
	mov   r8b, ' '			

.loop:
	movzx ecx, byte [rsi]		
	imul  eax, ecx, 0x01010101	
	movd  xmm0, eax
	pshufd xmm0, xmm0, 0		
	movdqu xmm1, [rsi]		
	pcmpeqb xmm0, xmm1	
	pmovmskb eax, xmm0	
	cmp   eax, 0xFFFF
	jne   .next			

	cmp   cl, r8b
	je    .next			
	mov   r8b, cl			
	cmp   cl, ' '
	je    .next			
	mov   [rdx], cl		
	inc   rdx

.next:
	add   rsi, 16
	sub   rdi, 16
	jnz   .loop
	ret

global ej4_get_numbers
; void ej4_get_numbers(size_t size, char numbers[10 * (size - 1) + 16], size_t output[size]);

ej4_get_numbers:
	mov    eax, 0x30303030		; 30 = ascii de '0'
	movd   xmm5, eax
	pshufd xmm5, xmm5, 0		; lleno a xmm5 de '0'
	mov    eax, 0x010A010A		
	movd   xmm6, eax
	pshufd xmm6, xmm6, 0		; lleno a xmm6 de 10, 1, 10, 1 ....
	mov    eax, 0x00010064		
	movd   xmm7, eax
	pshufd xmm7, xmm7, 0		; lleno a xmm7 de 100, 1, 100, 1...

.loop:
	movdqu xmm0, [rsi]		
	pmaxub xmm0, xmm5		; los blank space pasan a '0'
	psubb  xmm0, xmm5		; voy restando '0' a los lugares para pasar de ascii a enteros
	pslldq xmm0, 6			
	pmaddubsw xmm0, xmm6		; une los digitos en numeros de dos cifras 
	pmaddwd   xmm0, xmm7		; de dos a cuatro cifras

	pextrd eax, xmm0, 1		; 2 dígitos más significativos
	pextrd ecx, xmm0, 2		; 4 dígitos del medio
	pextrd r8d, xmm0, 3		; 4 dígitos menos significativos
	imul  rax, rax, 100000000
	imul  rcx, rcx, 10000
	add   rax, rcx
	add   rax, r8			
	mov   [rdx], rax

	add  rsi, 10			; paso al siguiente
	add  rdx, 8
	dec  rdi
	jnz  .loop
	ret