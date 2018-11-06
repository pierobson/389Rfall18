#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
pswds = open("passwords.txt", 'a+')

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase
count = 1
for salt in salts:
    #print('----- '+ salt + ' -----')
    wordlist = open("pwd.txt", 'r')
    for word in wordlist:
        count += 1
        h = hashlib.sha512()
        pw = salt + word.strip()
#        print(pw)
        h.update(pw)
        hsh = h.hexdigest()
#        print(hsh)
        hashes = open("../hashes", 'r')
        for hashpass in hashes:
            if hsh == hashpass.strip():
                l = pw + " == " + hashpass + "\n\n"
                print(l)
                pswds.write(l)
#print(count)
