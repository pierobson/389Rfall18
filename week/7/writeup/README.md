Writeup 7 - Forensics I
======

Name *Pierce Robson*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Pierce Robson*

## Assignment 7 writeup

### Part 1 (40 pts)

1. JPEG  

2. 41º53'55.0"N 87º37'22.4"W  
Chicago, Illinois. Regus - John Hancock Center

3. datetime=2018:08:22 11:33:24

4. iPhone 8 back camera 3.99mm f/1.8

5. 539.5m Above Sea Level 

6. Found through strings: CMSC389R-{look_If0und_a_string}  
Found from binwalk --dd="png:png" image: CMSC389R-{abr@cadabra}  


### Part 2 (55 pts)

CMSC389R-{dropping_files_is_fun}

First, I ran file on the binary and saw it was an ELF so I switched over to my Arch install. Then, I tried just running strings on it but got nothing useful out of it.  I decided to open the binary in r2 and started to look through the main function.  I first noticed that a bunch of characters get moved around and saw that they created the string “/tmp/.stego”.  Lower down, I saw that this file gets opened and some stuff gets written to it.  I tried opening the binary in gdb with gef in order to figure out what was being written to the file but that didn’t result in anything of use.  Next, I just ran the binary and tried to checkout the /tmp/.stego file.  However, nothing seemed to know what the heck .stego was.  I tried to binwalk the stego file and for some reason wasn’t able to extract anything, but it did tell me that it thought it found a JPEG with JFIF standard 1.01. Also, it said that this file started with the second byte (index 0x1).  Next, I opened the file with ghex and looked up the JFIF wiki page to see what the header should be.  Indeed, the header matched, but there was a null byte at the start of the file.  Lastly, I used dd to remove the first byte of the file (dd bs=1c skip=1 if=stego of=trim_stego) and got the flag in the out.txt file.

