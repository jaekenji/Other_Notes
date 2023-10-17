#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '10.50.44.215'
p = 12345

s.connect((ip,p))

s.send(b'Hello World!\n')

response, conn = s.recvfrom(1024)

print(response.decode())

