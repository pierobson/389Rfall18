#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
from pwn import *
import hashlib
import subprocess
context.log_level = 'error'

r = remote('142.93.117.193', 7331)

for i in range(0,10):
    # receive some data
    print(r.recvuntil(' the '))
    hash_type = r.recvuntil(' ').strip()
    print(hash_type)
    print(r.recvuntil('of '))
    data = r.recvline().strip()
    print(data)
    h = hashlib.new(hash_type)
    h.update(data)
    hsh = h.hexdigest()
    print(hsh)
    r.sendline(hsh)

print(r.recvall())
