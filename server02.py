import socket


port= 2020
deviceName= socket.gethostname()
serverIP= socket.gethostbyname(deviceName)


ServerSocketAdd=(serverIP, port) 
initialBufferSize= 16

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

server.bind(ServerSocketAdd)


server.listen()
print("server is Listening")

conn, addr= server.accept()

connected=True

while connected:
    msg_length=conn.recv(initialBufferSize).decode("utf-8")
    if msg_length:
        msg_length= int(msg_length)
        msg=conn.recv(msg_length).decode("utf-8")
        vowels = "aeiouAEIOU"
        count = 0
        for i in msg:
            if i in vowels:
                count += 1
        if count == 0:
            conn.send("Not enough vowels".encode("utf-8"))
        elif count <= 2:
            conn.send("Enough vowels".encode("utf-8"))
        else:
            conn.send("Too many vowels".encode("utf-8"))
conn.close()
            