section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        ;your code goes here!
        mov rcx, rdx

mem_loop:

        mov [rdi], sil  ; Move char into mem location
        add rdi, 1      ; Move to next mem location to copy to
        loop mem_loop   ; Loop until rcx == 0

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame


        ;;;;;;;;;;;;;;;;;;;;;
        ;your code goes here!
        ;;;;;;;;;;;;;;;;;;;;;
        mov rcx, rdx

strn_loop:
        
        mov al, byte [rsi+rcx-1]        ; Copy char from second arg to first arg
        mov byte [rdi+rcx-1], al              ; Increment pointer to both
        
        loop strn_loop          ; Loop until rcx == 0

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
