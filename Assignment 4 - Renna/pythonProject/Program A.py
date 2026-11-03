# Program Name: Program A.py
# Course: IT3883/Section W01
# Student Name: Brennan Renna
# Assignment Number: Assignment 4
# Due Date: 11/08/2026
# Purpose: Asks the user to enter a message, sends it to Program B, and displays the response.
# Resources Used: Course Material

import socket

# Both programs use the same address and port on this computer.
HOST = "127.0.0.1"
PORT = 50001

# Ask the user for the string that Program B will convert.
message = input("Enter a string: ")

# Create a TCP socket and connect to Program B.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    # Encode the text as bytes and send the entire message.
    client.sendall(message.encode("utf-8"))

    # Tell Program B the message is complete, while still allowing a reply.
    client.shutdown(socket.SHUT_WR)

    # Collect the reply in chunks until Program B closes its connection.
    response_parts = []
    while True:
        part = client.recv(1024)
        if not part:
            break
        response_parts.append(part)

# Join the received bytes, convert them to text, and display the reply.
response = b"".join(response_parts).decode("utf-8")
print("Response from Program B:", response)
