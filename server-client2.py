import socket
import threading 
import time

FORMAT = "utf-8"
IP = "127.0.0.1"
PORT = 50100
nextPort = 50200
ADDR = (IP, PORT)
ADDR_to_connect_to = (IP, nextPort)
server_lst = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

lst = []
data = ""
msg = ""

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(10)
    client.connect(ADDR_to_connect_to)
    return client

def startclient():
    client = connect()
    
    if (len(lst) > 0):
        senddata(client)
    else:
        sendinput(client)

def senddata(client):
    client.send(bytes(lst[0], FORMAT))

def sendinput(client):
    client.send(bytes(msg, FORMAT))

def startserver():
    con, add = server.accept()
    data = con.recv(1024).decode(FORMAT)
    lst.append(data)
    if(data != msg):   
        print(data)
    else:
        print("DATA SUCCESSFULLY CIRCLED THE RING")

thread = threading.Thread(target=startserver)
thread.start()
startclient()