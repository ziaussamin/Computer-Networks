import socket

port= 2020
deviceName= socket.gethostname()
serverIP= socket.gethostbyname(deviceName)


ServerSocketAdd=(serverIP, port) 


client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ServerSocketAdd)
initialBufferSize= 16

def send(msg):
    
    message = msg.encode("utf-8")
    msg_length = len(message) 
    send_length = str(msg_length).encode("utf-8")
    send_length+=b' '*(initialBufferSize-len(send_length))
    
    client.send(send_length)
    client.send(message)
    print(client.recv(128).decode("utf-8"))
    

send(f"Client's IP Address is {serverIP} and Client's Device name is {deviceName}")
