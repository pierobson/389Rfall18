#!/usr/bin/env python2

import sys
import struct
from datetime import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

sys.stdout = open('rep.txt', 'w')

# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version, timestamp, author, section_c = struct.unpack("<LLL8sL", data[0:24])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %d - %s" % (int(timestamp), datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")))
print("AUTHOR: %s" % author)
print("SECTION COUNT: %d" % int(section_c))

print("-------- BODY --------")

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

curr = 24
section = 0

while(curr < len(data)):
    stype, slen = struct.unpack("<LL", data[curr:curr+8])
    curr += 8
    sect = data[curr:curr+slen]
    curr += slen
    section += 1

    if stype == 0x1:
        print("Section %d: SECTION_PNG - len=%d\n" % ((section),slen))
        with open("png_%d.png" % section, 'wb') as fl:
            fl.write("\211PNG\r\n\032\n")
            fl.write(sect)
        #print(sect)
    elif stype == 0x2:
        print("Section %d: SECTION_DWORDS - len=%d\n" % ((section),slen))
        dwords = []
        for i in range(0, int(slen/8)):
            dwords.append(sect[i*8:i*8+8])
        print(dwords)
    elif stype == 0x3:
        print("Section %d: SECTION_UTF8 - len=%d\n" % ((section),slen))
        print("%s\n" % sect)
    elif stype == 0x4:
        print("Section %d: SECTION_DOUBLES - len=%d\n" % ((section),slen))
        dbls = []
        for i in range(0, int(slen/8)):
            dbls.append(struct.unpack("<d", sect[i*8:i*8+8]))
        print(dbls)
    elif stype == 0x5:
        print("Section %d: SECTION_WORDS - len=%d\n" % ((section),slen))
        words = []
        for i in range(0, int(slen/4)):
            words.append(sect[i*4:i*4+4])
        print(words)
    elif stype == 0x6:
        if slen != 16:
            bork("Invalid section length - SECTION_COORD")
        print("Section %d: SECTION_COORD - len=%d\n" % ((section),slen))
        one,two = struct.unpack("<dd", sect)
        print("%d, %d" % (one,  two))
    elif stype == 0x7:
        if slen != 4:
            bork("Invalid section length - SECTION_REFERENCE")
        print("Section %d: SECTION_REFERENCE - len=%d\n" % ((section),slen))
        d = struct.unpack("<L", sect)
        print("%d" % d)
    elif stype == 0x9:
        print("Section %d: SECTION_ASCII - len=%d\n" % ((section),slen))
        print(sect)
    else:
        bork("Invalid section type")

print("Total sections: %d" % section)
