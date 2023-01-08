import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
server_socket.bind((host, port))

# queue up to 5 requests
server_socket.listen(5)

while True:
    # establish a connection
    client_socket, addr = server_socket.accept()

    print(f"Got a connection from {addr}")

    # send a thank you message to the client.
    client_socket.send(b"Thank you for connecting")

    # close the client connection
    client_socket.close()
