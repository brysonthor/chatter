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

try:
    conn.send('Welcome to Bryson\'s Chat room\r\n')

    data = conn.recv(BUFSIZE)

    while not data.lower().startswith('adios'):
        if data.lower().startswith('help'):
            conn.send('list of commands and syntax')
        elif data.lower().startswith("test:"):
            conn.send('test')
        elif data.lower().startswith("name:"):
            conn.send('name')
        elif data.lower().startswith("get"):
            conn.send('get')
        elif data.lower().startswith("push:"):
            conn.send('push')
        elif data.lower().startswith("getrange"):
            conn.send('get range')
        else:
            conn.send('did not understand')
        data = conn.recv(BUFSIZE)
    conn.close()
except:
    conn.close()
