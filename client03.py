import socket


port= 2020
deviceName= socket.gethostname()
serverIP= socket.gethostbyname(deviceName)


ServerSocketAdd= (serverIP, port)
initialBufferSize= 16

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ServerSocketAdd)


def send(msg):
    
    message = msg.encode("utf-8")
    msg_length = len(message) 
    send_length = str(msg_length).encode("utf-8")
    send_length+=b' '*(initialBufferSize-len(send_length)) #finding the remaining length
    
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode("utf-8"))
    
connected = True
while connected:
    input_message = input("Please enter your message\n")
    send(input_message)