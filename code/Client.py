####################################################
#  D1014636 潘子珉                                      									
####################################################
#import sys
import socket
import tkinter as tk
import threading

PORT = 8888
BUF_SIZE = 1024			# Receive buffer size

def createWindow():
    window = tk.Tk()
    window.title('Client')
    window.geometry("400x300")
    return window

def createController(window, target):
    frame = tk.Frame(window)
    frame.grid_columnconfigure(0, weight = 1)
    frame.grid_columnconfigure(1, weight = 1)
    ipLabel = tk.Label(frame ,text = "ip")
    ipLabel.grid(row = 0, column = 0)
    ipEntry = tk.Entry(frame)
    ipEntry.grid(row = 0, column = 1)
    ipEntry.insert(0, '127.0.0.1')
    numberLabel = tk.Label(frame ,text = "初始數值")
    numberLabel.grid(row = 1, column = 0)
    numberEntry = tk.Entry(frame)
    numberEntry.grid(row = 1, column = 1)
    start_btn = tk.Button(frame, text='連線', font = ("Times", 11, ""), command = lambda: client_start(target,ipEntry.get(),int(numberEntry.get())))
    start_btn.grid(row = 2, column = 0, pady = 10)
    clear_btn = tk.Button(frame, text='清除', font = ("Times", 11, ""), command = lambda: delete(target))
    clear_btn.grid(row = 2, column = 1, pady = 10)
    return frame

def client_start(listbox, hostname, val1):
    t = threading.Thread(target=main,args=(listbox, hostname, val1))
    t.start()
    
def createConsole(window):
    frame = tk.Frame(window)
    listbox = tk.Listbox(frame, font = ("Times", 11, ""))
    listbox.pack(side = "left", fill = "both", expand = True)
    scrollbar = tk.Scrollbar(frame, orient = "vertical", command = listbox.yview)
    scrollbar.pack(side = "left", fill = "both", expand = False)
    listbox.configure(yscrollcommand = scrollbar.set)
    return frame, listbox

def delete(listbox):
   listbox.delete(0,tk.END)
   
def append(listbox, txt, color = '#9c7f00'):
    listbox.insert(tk.END, txt)
    listbox.itemconfig(tk.END, { 'bg' :  color, 'fg' : '#fff'})

def main(listbox, hostname, val1):
    serverIP = socket.gethostbyname(hostname)
    cSocket.settimeout(0.01)
    def sendMsg():
        lastNumber=val1
        try:
            val1Str = str(val1)
            cSocket.sendto(val1Str.encode('utf-8'), (serverIP, PORT))
            append(listbox, consoleFmt % ("[send]", f"data: {val1Str}"), "#009c0d")
            server_reply, reServerIp = cSocket.recvfrom(BUF_SIZE)
            while server_reply:
                server_utf8 = server_reply.decode('utf-8')
                print(server_utf8)
                append(listbox, consoleFmt % ("[recv]", f"data: {server_utf8}"), "#00609c")
                server_count = int(server_utf8)
                if server_count == lastNumber-1:
                    if server_count > 0:
                        server_count -= 1
                        val1Str = str(server_count)
                        append(listbox, consoleFmt % ("[send]", f"data: {val1Str}"), "#009c0d")
                            
                        cSocket.sendto(val1Str.encode('utf-8'), reServerIp)
                        server_reply, reServerIp = cSocket.recvfrom(BUF_SIZE)  
                    else:
                        break
                    lastNumber=server_count
                else:
                    server_reply, reServerIp = cSocket.recvfrom(BUF_SIZE)  
        except socket.timeout:
            sendMsg()
    sendMsg()
    #append(listbox, consoleFmt % ("[socket close]",""))
    #cSocket.close()

window = createWindow()
consoleFmt = "%-25s %s"
console, listbox = createConsole(window)
controller = createController(window, listbox)
controller.pack(fill = "x", side = 'top')
console.pack(fill = "both", side = 'bottom', expand = True)
cSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
append(listbox, consoleFmt % ("[create socket]",""))
window.mainloop()