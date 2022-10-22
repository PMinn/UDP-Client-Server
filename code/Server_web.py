####################################################
#  D1014636 潘子珉                      									
####################################################
import socket
import tkinter as tk
import threading

import eel
eel.init('gui', allowed_extensions=['.js', '.html'])

PORT = 8888
backlog = 5
BUF_SIZE = 1024			# Receive buffer size

def main():
    # print('Waiting to receive message from client')
    client_msg, reClientIp = srvSocket.recvfrom(BUF_SIZE)
    while client_msg:
        client_utf8 = client_msg.decode('utf-8')
        # print(client_utf8)
        eel.writeServerMessage(client_utf8,f"{reClientIp[0]}:{reClientIp[1]}")
        client_count = int(client_utf8)
        client_count -= 1
        server_reply = str(client_count)
        srvSocket.sendto(server_reply.encode('utf-8'), reClientIp)
        client_msg, reClientIp = srvSocket.recvfrom(BUF_SIZE)

srvSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Starting up server on port: %s' % (PORT))
srvSocket.bind(('', PORT))
t = threading.Thread(target=main)
t.start()
eel.start('server.html', size=(500, 500),port=0)