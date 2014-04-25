#!/usr/bin/env python
# encoding: utf-8
import sys

my_addr = list()

try:
    for item in sys.argv:
        my_addr.append(item.replace("0x", ""))
    my_addr.pop(0)
except IndexError:
    print "[-] You must supply a string to the script ...!"
    sys.exit(1)

for item in my_addr:
    if len(str(item)) > 8:
        item = item[:-1]

    s = [ item[i:i+2] for i in range(0, len(item), 2) ]

    for a in s[::-1]:
        sys.stdout.write("\\x" + a.lower())
        sys.stdout.flush()
    print
