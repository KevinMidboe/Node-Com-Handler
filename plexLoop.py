from socket import *
from time import sleep
                  
host = '10.0.0.41'
port = 12000
 
clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.sendto('plex', (host, port))
message, address = clientSocket.recvfrom(1024)
print message


clientSocket.close()
