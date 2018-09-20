Writeup 3 - OSINT II, OpSec and RE
======

Name: *Pierce Robson*  
Section: *0101*  

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Pierce Robson*  

## Assignment 3 Writeup

### Part 1 (100 pts)

Vulnerablility 1 - Weak Password -  
  The username of the login prompt is easily guessed since it's just a shortened version of the username Fred Kreuger seems to use everywhere and the fact that the login prompt has no bruteforce prevention mean that the password can be easily bruteforced.  The password of "pokemon" doesn't help secure the server from this attack because "pokemon" is high up on some common wordlists used to crack passwords, including the rockyou.txt that we used.  Also, if the attacker knew about Fred's interests, they possibly could have guessed the password.  Now that we know the password is "pokemon", it seems obvious considering almost all of the posts on his Instagram page are of Pokemon.  Obviously, this is a problem because once the username and password are known, anyone can access the server on port 1337 where much of Cornerstone Airlines data are. This inlcudes potentially sensitive information such as the boarding passes found where the flag is. 
  
  In order to fix this issue, Fred should use a more secure password consisting of a long (minumum of 8) sequence of fairly random characters including special symbols (#$?;% etc.), numbers, and both lower and uppercase letters.  This minimizes the chance of the password appearing on a wordlist and makes bruteforcing take much longer or nearly impossible.  Next, Fred should implement some sort of bruteforce prevention system.  A simple way to do this is to timeout the user who is attempting to login after a given number of failed attempts, increasing the duration of the timeout each time it occurs.  This could be done by IP address so the attacker would need to change their IP if they wished to circumvent the timeout, which would add time to their attack.  Lastly, Fred could either blacklist IPs who fail to login after some number of attempts or whitelist IPs that he knows will be authorized users, such as himself.  This could be done by checking the validity of the IP that is connecting before presenting them with a login prompt.
  
  
  
Vulnerability 2 - Open Ports -
  To prevent access to the login prompt running on port 1337 in the first place, Fred should not allow an unauthorized user such as an attacker to find open ports on the server.  If I had never found that port 1337 was open, I never would have been able to try to login to the prompt.  To hide this 
