import socket


def server_program():
    host = socket.gethostname()
    port = 2020

    server_socket = socket.socket()

    server_socket.bind((host, port))

    server_socket.listen()
    print("Server is Listening")

    connecti, address = server_socket.accept()
    print("Connection from: " + str(address))


    data = connecti.recv(128).decode()

    data = int(data)
    pay = 0

    if (data <= 40):
        pay = data * 200
    elif (data > 40):
        pay = ((data - 40) * 300) + 8000

    data = str(float(pay)) + " TK"

    connecti.send(data.encode())

    print("Server closed")
    connecti.close()


server_program()
