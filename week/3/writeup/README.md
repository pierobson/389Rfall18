Writeup 3 - OSINT II, OpSec and RE
======

Name: *Pierce Robson*  
Section: *0101*  

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Pierce Robson*  

## Assignment 3 Writeup

### Part 1 (100 pts)

#### Vulnerablility 1 - Weak Password -  
  The username of the login prompt is easily guessed since it's just a shortened version of the username Fred Kreuger seems to use everywhere and the fact that the login prompt has no bruteforce prevention mean that the password can be easily bruteforced.  The password of "pokemon" doesn't help secure the server from this attack because "pokemon" is high up on some common wordlists used to crack passwords, including the rockyou.txt that we used.  Also, if the attacker knew about Fred's interests, they possibly could have guessed the password.  Now that we know the password is "pokemon", it seems obvious considering almost all of the posts on his Instagram page are of Pokemon.  Obviously, this is a problem because once the username and password are known, anyone can access the server on port 1337 where much of Cornerstone Airlines data are. This inlcudes potentially sensitive information such as the boarding passes found where the flag is. 
  
  In order to fix this issue, Fred should use a more secure password consisting of a long (minumum of 8) sequence of fairly random characters including special symbols (#$?;% etc.), numbers, and both lower and uppercase letters.  This minimizes the chance of the password appearing on a wordlist and makes bruteforcing take much longer or nearly impossible.  Next, Fred should implement some sort of bruteforce prevention system.  A simple way to do this is to timeout the user who is attempting to login after a given number of failed attempts, increasing the duration of the timeout each time it occurs.  This could be done by IP address so the attacker would need to change their IP if they wished to circumvent the timeout, which would add time to their attack.  Lastly, Fred could either blacklist IPs who fail to login after some number of attempts or whitelist IPs that he knows will be authorized users, such as himself.  This could be done by checking the validity of the IP that is connecting before presenting them with a login prompt.
  
  
  
#### Vulnerability 2 - Open Ports -
  To prevent access to the login prompt running on port 1337 in the first place, Fred should not allow an unauthorized user such as an attacker to find open ports on the server.  If I had never found that port 1337 was open, I never would have been able to try to login to the prompt.  To hide this, Fred should setup a firewall to filter incoming packets from unknown sources.  He could configure the firewall to only allow his personal network or could also allow connections from sources that appear to truly be Fred.  When an someone tries to scan the ports of the server's IP or attempts to nc to it, the firewall would simply drop the packets if they are deemed unauthorized.  This means that nmap wouldn't be able to find the open ports on the server and that attackers trying to connect to the open port 1337 would never get a connection.  Although Fred should always use a more secure password than pokemon, this basically solves the weak password issue as well because an attacker would never be able to get to the login prompt without somehow tricking the firewall into thinking they are Fred.
  
  (https://www.digitalocean.com/community/tutorials/what-is-a-firewall-and-how-does-it-work)
  
  
 #### Vulnerability 3 - Apache Vulnerabilities -  
  When looking up the 142.93.118.186 on Shodan, I discovered that the server is running an outdated version of Apache and is likely to be vulnerable to various attacks.  One of these includes bypassing SSL access restrictions.  
   '  
   CVE-2016-4979 	The Apache HTTP Server 2.4.18 through 2.4.20, when mod_http2 and mod_ssl are enabled, does not properly recognize the "SSLVerifyClient require" directive for HTTP/2 request authorization, which allows remote attackers to bypass intended access restrictions by leveraging the ability to send multiple requests over a single connection and aborting a renegotiation.
   '  
   In order to fix this, Fred should make sure all of the software he has running on the server is up to date with the latest version or patches.  
   
   (https://www.shodan.io/host/142.93.118.186)
