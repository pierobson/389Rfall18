Writeup 10 - Crypto II
=====

Name: Pierce Robson
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Pierce Robson

## Assignment 10 Writeup

### Part 1 (70 Pts)  
CMSC38R-{y0U-are_the_5ql_n1nja}  
First, I just started clicking around on the website to see if I could find any inputs that might be unsanitized, etc... I didn't find anything super exciting, but I did notice that the url for each item page included an id number.  I tried a bunch of different numbers, negative numbers, and words but couldn't find anything at first.  I still couldn't find anything else of interest on the website though so I kept trying. Instead of random numbers I started trying things that might have some meaning, 420, 8080, and eventually, 1337. It was with 1337 that I found the page with the flag.

  
### Part 2 (30 Pts)  
Level 1 - I literally just put an alert script, <script>alert()</script>, in the query box...   
Level 2 - I tried a couple different things for this one. First, I just tried to put the same alert script as level 1 but it didn't work. Next, I tried to make a link that would execute a script but that just ended up breaking EVERYTHING.  Lastly, I posted <button onClick='alert("boi")'>BOT</button> and when I clicked the button, I got the alert.  
Level 3 - I just tried putting alerts in the url of various forms until I got the alert with the input "2'/><script>alert()</script>"  
Level 4 - This one took me a little longer and I looked at the hints...  I kept trying to inject alerts as normal until I saw the hint about decoding.  I figured the semicolon was messing things up so I encoded it and enter "')%3balert('" which produced an alert.  
Level 5 - I noticed the next parameter in the url is used to designate what page should be loaded when the Next link is clicked.  I had to look up how to make a link run JS without changing the onClick and found that inputing "javascript:alert()" made the alert pop up.  
Level 6 - Lastly, I spent a long time on this one trying to get an alert to pop up.  Nothing I tried involving direct injection worked and I eventually checked the hints.  I saw the google api hint and noticed that whatever the callback is in the url gets called at the end of the function. I changed foo to alert and tried that as the url but the https was filtered. I checked the source for how it was filtered and noticed it was case sensitive. I changed https to HTTPS and got the alert to work.  

