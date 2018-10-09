Writeup 5 - Binaries I
======

Name: *Pierce Robson*
Section: *0101*

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Pierce Robson*

## Assignment 5 Writeup

Memset:  
    Memset was really simple to implement, however it took some time before I realized that using rsi for the  
    single char wasn't working.  Since it is 64bit, rsi is too big and moving from rsi into an offset of rdi  
    moves more than the single char that I expected.  I just move rdx into the counter rcx, copy sil, which  
    I found is just the low 8 bits of rsi, into an offset of rdi, and then increment rdi.  This then loops  
    and the loop will end when rcx hits 0.  It took me forever to figure out that rsi wasn't working properly  
    and that I had to use sil instead.  
  

Strncpy:  
    I thought this would be more difficult than memset, but it took so long for me to figure out why  
    my memset wasn't working that this ended up being the easier of the two.  I again just move rdx into  
    rcx.  Then, I copy rcx bytes from rsi to rdi in reverse order.  This is because I just use rcx as the  
    offset from the beginning of the strings which starts high and decrements to 0.  However, the loop will  
    stop when rcx == 0 so I have to use rcx - 1 to make sure that it copies the first char and not past the end.  


Debugging:  
    I used the GEF extension of gdb to help with debugging.  This was nice because everytime I step  
    the program, it prints a whole bunch of info at the same time which helps speed up debug time.  
    It came in most handy when realizing that using rsi for memset wouldn't work.  Another big  
    problem I had was testing my code on my desktop in Arch.  Even after changing rsi to sil for memset,  
    it doesn't work and when rsi gets set for strncpy it gets set to 0... I never figured out why that happens  
    but the code works in Kali so I haven't spent anymore time looking into it.