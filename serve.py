#!/usr/bin/python
from socket import *
HOST = ''
PORT = 9020
ADDR = (HOST,PORT)
BUFSIZE = 4096

#create an INET, STREAMing socket
serversocket = socket(AF_INET,SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
serversocket.bind((ADDR))
#become a server socket
serversocket.listen(2)

print 'waiting for connection request'

conn,addr = serversocket.accept()
print 'it is now connected'

conn.send('Welcome to Bryson\'s Chat room\r\n')

data = conn.recv(BUFSIZE)
while data.lower() != 'adios\r\n':
    if data == 'help\r\n':
            conn.send('list of commands and syntax')
    elif data == '


conn.close()
