# the client end

import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("server_ip", 12345))

# Send and receive messages
while True:
    message = input("You: ")
    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print(f"Server: {response}")

# Close the connection
client_socket.close()
