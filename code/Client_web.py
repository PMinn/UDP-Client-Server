####################################################
#  D1014636 潘子珉                                      									
####################################################
#import sys
import socket
import tkinter as tk
import threading

import eel
eel.init('gui', allowed_extensions=['.js', '.html'])

PORT = 8888
BUF_SIZE = 1024			# Receive buffer size

@eel.expose
def main(val1,hostname = "127.0.0.1"):#listbox, 
    serverIP = socket.gethostbyname(hostname)
    cSocket.settimeout(0.01)
    def sendMsg():
        lastNumber=int(val1)
        try:
            val1Str = str(val1)
            cSocket.sendto(val1Str.encode('utf-8'), (serverIP, PORT))
            server_reply, reServerIp = cSocket.recvfrom(BUF_SIZE)
            while server_reply:
                server_utf8 = server_reply.decode('utf-8')
                # print(server_utf8)
                eel.writeClientMessage(1,server_utf8)
                server_count = int(server_utf8)
                if server_count == lastNumber-1:
                    if server_count > 0:
                        cSocket.sendto(server_reply, reServerIp)
                    else:
                        eel.connectEnd()
                        break
                    lastNumber=server_count
                server_reply, reServerIp = cSocket.recvfrom(BUF_SIZE)  
        except socket.timeout:
            eel.writeClientMessage(-1, val1)
            sendMsg()
    sendMsg()
    
cSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
eel.start('client.html', size=(500, 500),port=0)  # Start