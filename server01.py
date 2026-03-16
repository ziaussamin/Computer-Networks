
import socket

port= 2020
deviceName= socket.gethostname()
serverIP= socket.gethostbyname(deviceName)


ServerSocketAdd=(serverIP, port) 

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ServerSocketAdd)



server.listen()

conn, addr= server.accept()

connected=True

while connected:
    msg_length=conn.recv(128).decode("utf-8")
    if msg_length:
        msg_length= int(msg_length)
        msg=conn.recv(msg_length).decode("utf-8")

        print(msg)
        conn.send("Meesage Received".encode("utf-8"))
conn.close()
            