# this is the server side

import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP and port
server_socket.bind(("your_server_ip", 12345))

# Listen for incoming connections
server_socket.listen()

print("Server is listening...")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Receive and send messages
while True:
    message = client_socket.recv(1024).decode()
    print(f"Client: {message}")
    response = input("You: ")
    client_socket.send(response.encode())

# Close the connection
client_socket.close()
