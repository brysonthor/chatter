#!/usr/bin/python
from socket import *

HOST = 'localhost'
PORT = 9020
ADDR = (HOST,PORT)
BUFSIZE = 4096

#create an INET, STREAMing socket
s = socket(AF_INET, SOCK_STREAM)
#now connect to the web server on port 9020
# - the normal http port
s.connect((ADDR))

data = s.recv(BUFSIZE)
print data

s.close()

