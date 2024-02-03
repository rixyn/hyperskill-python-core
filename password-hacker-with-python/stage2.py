import socket
import sys
from itertools import product
from string import ascii_lowercase, digits

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


def generate_passwords():
    # Define the character set to use for the password
    charset = ascii_lowercase + digits
    for length in range(1, 6):  # Iterate over different password lengths
        # Generate all combinations for current length
        for attempt in product(charset, repeat=length):
            # Yield each combination as a potential password
            yield ''.join(attempt)


def try_passwords(socket):
    for password in generate_passwords():  # Iterate over the generator function
        socket.send(password.encode())  # Send the password to the server
        response = socket.recv(1024).decode()  # Receive the server's response
        if response == "Connection success!":  # If the password is correct
            print(password)  # Print the correct password
            break
        elif response == "Too many attempts":  # If too many attempts have been made
            print("Too many attempts, exiting.")
            break


try_passwords(client_socket)  # Start trying passwords

client_socket.close()  # Close the socket connection
