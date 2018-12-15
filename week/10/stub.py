#!/usr/bin/env python2
# from the git repo
import md5py
from pwn import *
context.log_level = 'error'
#####################################
### STEP 1: Calculate forged hash ###
#####################################

message = 'msg'    # original message here

r = remote('142.93.118.186', 1234)
r.recvuntil('>>>')
r.send('1\n')
r.recvuntil('>>>')
r.send(message + '\n')
r.recvuntil('Your hash: ')
legit = r.recvline().strip()       # a legit hash of secret + message goes here, obtained from signing a message

print(legit)

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'YEET'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print(fake_hash)


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits
for i in range(6,16):
    padding = '\x80'
    padding +=  '\x00' * (53 - i) 
    padding += chr(8 * (i+2)) + '\x00'*7
    
# payload is the message that corresponds to the hash in `fake_hash`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = fake_hash
    payload = message + padding + malicious

# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!

    r.send('2\n')
    r.recvuntil('>>>')
    r.send(fake_hash + '\n')
    #print('Sent ->' + fake_hash)
    r.recvuntil('>>>')
    r.send(payload + '\n')
    while True:
        resp = r.recvline().strip()
        print(resp)
        if "I've either signed" in resp:
            break

