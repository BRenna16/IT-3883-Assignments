# Program Name: Program B.py
# Course: IT3883/Section W01
# Student Name: Brennan Renna
# Assignment Number: Assignment 4
# Due Date: 11/08/2026
# Purpose: Receives the message, converts it to uppercase, and sends it back to Program A.
# Resources Used: Course Material

import socket

# Match the address and port used by Program A.
HOST = "127.0.0.1"
PORT = 50001

# Create a TCP socket that listens for Program A on this computer.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Program B is waiting on {HOST}:{PORT}...")

    # Accept one connection and automatically close it when finished.
    connection, address = server.accept()
    with connection:
        # Receive every chunk until Program A finishes sending.
        message_parts = []
        while True:
            part = connection.recv(1024)
            if not part:
                break
            message_parts.append(part)

        # Decode the complete message and convert it to uppercase.
        message = b"".join(message_parts).decode("utf-8")
        response = message.upper()
        print("Received from Program A:", message)
        print("Sending back:", response)

        # Send the uppercase response before the connection closes.
        connection.sendall(response.encode("utf-8"))
