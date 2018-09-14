Writeup 2 - OSINT (Open Source Intelligence)
======

Name: *Pierce Robson*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Pierce Robson*

## Assignment 2 writeup

### Part 1 (45 pts)

1. Fred Krueger

2.  Possible Reddit account - u/kruegster1990 - Found just by google searching kruegster1990  
  
    Twitter - @kruegster1990                  - Found by googling kruegster1990 and following link to   
        swtity.com/umdcsec/following.  
            - Lives in Silver Spring, MD according to Twitter account.  
            - Born in 1990 according to Twitter and his username lol.
    
    Instagram - @kruegster1990                - Decided to search some random other social media sites in case  
    google missed anything. Nothing for pinterest, youtube, etc. but did find and Instagram account with the same  
    picture as the Twitter account.
              
    Email   - kruegster@tutanota.co           - Found on About page of website. Website found in Twitter bio. 
      

3. IP Address - 142.93.118.186  
Found by executing '*ping cornerstoneairlines.co*' and seeing '*64 bytes from 142.93.118.186...*'

4. Found robots.txt which mentioned a hidden directory /secret which contained a flag in the source and found a flag in the home page's source.  
robots.txt also appears to say something about user access to /secret.  
Full report from DirBuster can be found under dirbust_cornerstoneairlines.txt.  
CMSC389R-{h1dden_fl4g_in_s0urce}  
CMSC389R-{fly_th3_sk1es_w1th_u5}  

5. Yes, found 142.93.117.193 which is the Admin page of the website and says its under construction.  
I'm still confused about this page though because it has a comment in the source that says "Keep looking, class! You're very close :)"  
but I never found anything that seemed to be related to this... 

6. whois cornerstoneairlines.co gives 1234 Secure Road, New York, NY. Searching 142.93.118.186 on censys  
also says New York, NY and that the network is run by DIGITALOCEAN-ASN - DigitalOcean, LLC.  
Using discover, however, I got an address of 101 Ave of the Americas, 10th Floor, New York, NY, and I think  
this is probably more accurate than the other address.

7. Searching 142.93.118.186 on censys first showed me that the server is running Ubuntu and Shodan confirmed this  
by listing an OpenSSH service specific to Ubuntu.

8. Found using dnsdumpster.com -> *CMSC389R-{dns-txt-rec0rd-ftw}*

### Part 2 (55 pts)

*CMSC389R-{c0rn3rstone-air-27670}*  
Most of my strategy to get access to the server was based on the assumption that the Kruegster would  
continue to use the same username for the admin server as he did for everything else.  
Because of this, I ran my script in 6 separate processes with slight modifications to each.  
I used 3 different usernames, kruegster1990, kruegster, and admin, while starting a script at the beginning of  
the wordlist and another 1000 lines in to the wordlist for each name.  
  
To write the script, I used pwntools to make connecting to the server just a little bit easier.  
The script opens the wordlist and a log file.  Then, it just iterates over the lines of the list  
trying each as a password.  If the response to the username and password did not come back as 'Fail',  
the username, password, and response are written to the log and the program exits.  
  
In total, the scripts ran for about 10 minutes before I noticed one had stopped.  I checked the log and sure enough,  
the kruegster username had found the correct password, pokemon.  
  
Once I had the password, I nc'ed into the server and ls'ed.  I wasn't sure where to look at first but I figured  
home would be a good place to start.  Home only had the flight_records directory so that seemed promising.   
In the flgiht records folder, I got a little concerned with all the txt files but I remembered seeing the boarding  
pass on the kruegster1990 instagram account.  The second picture has an AAC number on it, so I checked the  
txt file with the matching number and found the flag.
