import socket
import threading

port= 2020
deviceName= socket.gethostname()
serverIP= socket.gethostbyname(deviceName)


ServerSocketAdd=(serverIP, port) 
initialBufferSize= 16

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

server.bind(ServerSocketAdd)


server.listen()




def handle_clients(serversocket, clientsocket):
    connected=True
    
    while connected:
        msg_length=serversocket.recv(16).decode("utf-8")
        if msg_length:
            msg_length= int(msg_length)
            msg=serversocket.recv(msg_length).decode("utf-8")

            vowels = "aeiouAEIOU"
            count = 0
            for i in msg:
                if i in vowels:
                    count += 1
            if count == 0:
                serversocket.send("Not enough vowels".encode("utf-8"))
            elif count <= 2:
                serversocket.send("Enough vowels".encode("utf-8"))
            else:
                serversocket.send("Too many vowels".encode("utf-8"))
    serversocket.close()

def start():
    server.listen()
    print("Server is listening")
    while True:
        serversocket, clientsocket= server.accept()
        thread=threading.Thread(target=handle_clients,args=(serversocket, clientsocket))
        thread.start()
start()