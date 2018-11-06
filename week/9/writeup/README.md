Writeup 9 - Crypto I
=====

Name: Pierce Robson
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Pierce Robson

## Assignment 9 Writeup

### Part 1 (60 Pts)  
My script for [part one](part1.png) just iterates over every char in the provided string and every word in the wordlist, prepends the char to the word, checks the hash of that password against all 4 hashes, writes and prints it if it matches any, and continues for all possible conmbinations.  By the end of these combinations, all 4 hashes had been cracked.  I had to change the wordlist file to use my own instead of the one provided because I assume the provided one was just a wget of the file which didn't work and provided the html for the page of the list.


### Part 2 (40 Pts)  
CMSC389R-{H4sh-5l!ngInG-h@sH3r}    
  
The first thing I did for [part two](part2.png) was just nc to the server and see what the trivia thing was all about.  Unfortunately, I didn't read the instructions carefully and wrote a script to try to find the plaintext that hashes to the value given from the server.... Once I saw that hashcat wasn't happy with the input I gave it, I read the instructions again and saw that I was just supposed to be calculating the hashes of the given input for the given hash function.  Once I noticed that, the script became much more simple.  
  
My script just waits for input from the server, gets the hash function and input for the hash function, calculates the hash, sends it back to the server, and repeats for a total of 10 iterations.  Then, it breaks out of the loop because there are only 10 questions and receives the rest of the data from the server, which prints the flag.

