#!/usr/bin/python3

import socket
import sys
from struct import *

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
except socket.error as msg:
    print(msg)
    sys.exit()

packet = ''

src_ip = '10.1.0.2'
dst_ip = '10.3.0.2'

ip_ver_ihl = 69
ip_tos = 0
ip_len = 0
ip_id = 12345
ip_frag = 0
ip_ttl = 64
ip_proto = 6
ip_check = 0
ip_srcadd = socket.inet_aton(src_ip)
ip_dstadd = socket.inet_aton(dst_ip)

ip_header = pack('!BBHHHBBH4s4s', ip_ver_ihl, ip_tos, ip_len, ip_id, ip_frag, ip_ttl, ip_proto, ip_check, ip_srcadd, ip_dstadd)

message = b'HELLOWORLD!!1!!1!'
packet = ip_header + message

s.sendto(packet, (dst_ip, 0))
