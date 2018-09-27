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
  
To run my script, just execute `python exp.py` (python 2.7 not python3).
The script uses pwntools which may be installed via pip with `pip install --upgrade pwntools`.
This will then drop you into the script and allow you to enter the commands.  
  
Both the shell and pull commands posed challenges in this part. 
  
For the shell command, it first connects to the server and waits for input from the user.  
Then, it inserts the input into a specially formatted string and sends this to the server, injecting the commands.  
To get the fully interactive functionality, the script keeps track of the working directory at the end of each command executed.  
The string mentioned earlier first cd's to this dir, executes the user's command, and then prints the directory again.  
The script ignores the first 300 chars of the response because that is the ping, prints the output of the user's command,  
and then reads and updates the stored working directory.  
  
For the pull command, I first tried to use scp locally which didn't work because I don't have the root password for the server,  
and to inject an scp command to directly copy the file to the user's machine, but I could never get it to work.  
I don't know if this is because the scp command fails to execute on the server, if it was an issue with my network blocking  
the incoming file, or because I was just doing it incorrectly, but I gave up on scp.  
What did work, was to inject a cat command to read the contents of the file and write that to a local file.  
I'm not 100% positive that this works with binary files but it appears that it does.  
Since the binaries on the server are ELF files, I couldn't execute them on my macbook without tossing them in a vm.  
However, pulling /bin/cat and trying to execute it does ask for root permissions before saying it can't find the command,  
so I'm pretty sure it would work if I tried it on a Linux machine.  
