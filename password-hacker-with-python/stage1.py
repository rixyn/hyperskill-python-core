import sys
import socket

args = sys.argv

hostname = args[1]
port = int(args[2])
address = (hostname, port)
data = args[3]


with socket.socket() as client_socket:

    client_socket.connect(address)

    data = data.encode()

    client_socket.send(data)

    response = client_socket.recv(1024)

    response = response.decode()

    print(response)
