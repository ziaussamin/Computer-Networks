import socket



def client_program():

    host = socket.gethostname()

    port = 2020

    client_socket = socket.socket()

    client_socket.connect((host, port))

    message = input("Enter amount of hours person works: ")

    client_socket.close()



client_program()
