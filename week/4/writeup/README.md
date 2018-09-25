Writeup 3 - Pentesting I
======

Name: *Pierce Robson*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Pierce Robson*

## Assignment 4 Writeup

### Part 1 (45 pts)  
Flag: CMSC389R-{p1ng_as_a_$erv1c3}  
Input: `8.8.8.8; cd home; cat flag.txt`   
  
First, I just tried to ping the localhost with 127.0.0.1 just to see what would happen.  Nothing special so I tried a Google server, 8.8.8.8.  
Still nothing super interesting but I figured I'd try the simplest command injection I could think of which was just giving it some extra commands to run.  
To do this, I first tried `8.8.8.8; ls` and saw that it executed the ls command and showed me the output.  
I figured if there was a flag txt file somewhere, it was most likely in the home directory so my next attempt was  
`8.8.8.8; cd home; ls` which greeted me with a 'flag.txt' file.  
Lastly, I connected one more time and gave it `8.8.8.8; cd home; cat flag.txt` which gave me the flag.  
All in all, it probably took about 3 minutes to get the flag.  
  
I found the script being run on port 45 in the opt directory with the name of 'container_startup.sh'.  
Finding this script was by far the longest piece of this part.  At first I assumed it would be in the home directory  
with the flag.txt file, but the flag was the only thing there, including hidden files.  
I eventually found this by injecting `8.8.8.8; cd "somedir"; ls` for all directories  
in the root directory and looking into anything suspicious in those folders until I found this bash script.  
I spent a lot of time looking in the bin and sbin directories but I really had no idea where I should've been looking.
This script takes the input and just evaluates `ping -w 5 -c 2 $input` for whatever the input is. 
This is why it is possible to execute arbitrary commands.  
A simple way to fix this is to wrap `$input` in single quotes so that the entire input is treated as the argument to the ping command instead of  
executing the ping and then arbitrary code.  

### Part 2 (55 pts)
*Put your writeup >= 200 words here in response to part 2 prompt. Your code for part 2 should be copied into a file in the /writeup directory and pushed there as well*
