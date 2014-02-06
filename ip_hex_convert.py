#!/usr/bin/env python
# encoding: utf-8

import sys
import argparse

def ip2hex(ip):
    try:
        hex_reverse  = "0x" + "".join(map(lambda x: hex(int(x))[2:].zfill(2), ip.split(".")))
        hex_nreverse = "0x" + "".join(map(lambda x: hex(int(x))[2:].zfill(2), ip.split(".")[::-1]))
        hex_opcodes  = "".join(map(lambda x: "\\x%02x" % int(x), ip.split(".")))
        print "\nHex reverse    : %s\t\t(%s)" % (hex_reverse, hex2ip(hex_reverse.replace('0x', '')))
        print "Hex non reverse: %s\t\t(%s)" % (hex_nreverse, hex2ip(hex_nreverse.replace('0x','')))
        print "Hex in opcodes : %s\t(%s)\n" % (hex_opcodes, opt.ip)
    except ValueError as e:
        print "[-] You probably gave a bad value !"
        print "[-] ERROR: %s" % e
        sys.exit(2)


def hex2ip(ip):
    try:
        return '.'.join(str(int(i, 16)) for i in reversed([ip[i:i+2] for i in range(0, len(ip), 2)]))
    except ValueError as e:
        print "[-] You probably gave a bad value !"
        print "[-] ERROR: %s" % e
        sys.exit(2)


def port2hex(port):
    try:
        port_hex = hex(int(port)).replace("0x", "")
        port_hex_op = [ port_hex[i:i+2] for i in range(0, len(port_hex), 2) ]
        port_hex_op =  "".join("\\x" + x for x in port_hex_op)
    except ValueError as e:
        print "[-] You probably gave a bad value !"
        print "[-] ERROR: %s" % e
        sys.exit(2)
    return ( port_hex_op, port_hex )

if __name__ == "__main__":
    desc  = "Convert ip to hex and back to text"
    parser = argparse.ArgumentParser(description=desc, add_help=True)
    parser.add_argument('-x', '--hex', action="store_true", help='convert ip to hex')
    parser.add_argument('-t', '--text', action="store_true", help='convert hex ip to text')
    parser.add_argument('-i', '--ip', dest="ip", help='the ip address to convert')
    parser.add_argument('-p', '--port', dest="port", help='the network port to convert')
    opt = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if opt.hex and opt.ip:
        ip2hex(opt.ip)

    if opt.text and opt.ip:
        print "\nIP: %s\n" % hex2ip(opt.ip)

    if opt.port:
        port_hex_op, port_hex = port2hex(opt.port)
        print "\nHex reverse: 0x%s" % port_hex
        print "Hex opcodes: %s\n" % port_hex_op

#EOF
