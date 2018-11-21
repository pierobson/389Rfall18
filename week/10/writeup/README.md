Writeup 10 - Crypto II
=====

Name: Pierce Robson
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Pierce Robson

## Assignment 10 Writeup

### Part 1 (70 Pts)  
CMSC389R-{i_still_put_the_M_between_the_DV}  
Legit Hash: a1f519ffcbbfceba78ae6e1d2cb64886  
Crafted Message: 'msg\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x00\x00\x00\x00\x00\x00\x00YEET'  
Crafted Hash: 9b59b757134577496a99d38b697e547d  
Payload Sent: a1f519ffcbbfceba78ae6e1d2cb64886  

I basically just went through the slides and implemented what the stub code told us to do... I used pwntools for sockets to make sockets a little simpler.

### Part 2 (30 Pts)
  
Generating Keys -> gpg --gen-key  
Importing Public Keys -> gpg --import pubkeyname  
Encrypting Message -> gpg -e -u "Your name" -r "The name in the key you imported" filewithmessage  



