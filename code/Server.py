####################################################
#  D1014636 潘子珉                      									
####################################################
import socket
import tkinter as tk
import threading

PORT = 8888
backlog = 5
BUF_SIZE = 1024			# Receive buffer size


def createWindow():
    window = tk.Tk()
    window.title('Server')
    window.geometry("400x300")
    return window

def createController(window, target):
    frame = tk.Frame(window)
    frame.grid_columnconfigure(0, weight = 1)
    frame.grid_columnconfigure(1, weight = 1)
    start_btn = tk.Button(frame, text='開始', font = ("Times", 11, ""), command = lambda: server_start(target,start_btn))
    start_btn.pack(side = "left",ipadx = 20, padx = 10, pady = 10)
    clear_btn = tk.Button(frame, text='清除', font = ("Times", 11, ""), command = lambda: delete(target))
    clear_btn.pack(side = "left",ipadx = 20, padx = 10, pady = 10)
    return frame

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

def main(listbox, btn):
    print('Waiting to receive message from client')
    client_msg, reClientIp = srvSocket.recvfrom(BUF_SIZE)
    while client_msg:
        client_utf8 = client_msg.decode('utf-8')
        print(client_utf8)
        append(listbox, consoleFmt % ("[recv]", f"{reClientIp[0]}:{reClientIp[1]}", f"data: {client_utf8}"), "#00609c")
        client_count = int(client_utf8)
        # Send message to client
        client_count -= 1
        server_reply = str(client_count)
        append(listbox, consoleFmt % ("[send]", f"{reClientIp[0]}:{reClientIp[1]}", f"data: {server_reply}"), "#009c0d")
        #client.send(server_reply.encode('utf-8'))
        srvSocket.sendto(server_reply.encode('utf-8'), reClientIp)
        client_msg, reClientIp = srvSocket.recvfrom(BUF_SIZE)
    # Close the TCP socket
    #append(listbox, consoleFmt % ("[socket close]","",""))
    #btn["state"] = tk.NORMAL
    #client.close()
    #srvSocket.close()
# end of main

def server_start(listbox, btn):
    btn["state"] = tk.DISABLED
    t = threading.Thread(target=main,args=(listbox, btn))
    t.start()
    

window = createWindow()
consoleFmt = "%-16s %20s   %s"
console, listbox = createConsole(window)
controller = createController(window, listbox)
controller.pack(fill = "x", side = 'top')
console.pack(fill = "both", side = 'bottom', expand = True)
srvSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
append(listbox, consoleFmt % ("[create socket]","",""))
print('Starting up server on port: %s' % (PORT))
srvSocket.bind(('', PORT))
append(listbox, consoleFmt % ("[bind]","", f" port: {PORT}"))
window.mainloop()