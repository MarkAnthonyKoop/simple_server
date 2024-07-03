import socket
import subprocess
import os
import signal
import time

# Creating a socket
def create_server_socket(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(1)
    return server_socket

# Handling connection and commands
def handle_client_connection(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if data == 'restart':
            print("Received restart command. Restarting...")
            os.kill(os.getpid(), signal.SIGTERM)
        elif data:
            print(f"Received command: {data}")
            subprocess.run(data.split())

# Main function to run the server
def run_server(port):
    print("Server starting...")
    server_socket = create_server_socket(port)
    print(f"Listening on port {port}...")
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    handle_client_connection(client_socket)

if __name__ == '__main__':
    run_server(5000)
