'''
CS 3700 - Networking & Distributed Computing - Fall 2024
Instructor: Thyago Mota
Student:
Description: Homework 04 - UDP Game
'''
import sys
import socket
import random
HOST = '127.0.0.1'
PORT = 4000
BUFFER = 1024
READY = 0
BUSY = 1
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    
    print(f"Ready to play {HOST}:{PORT}")
    
    state = READY
    secret_number = None
    client_address = None
    attempts = 0
    while True:
        data, address = server_socket.recvfrom(BUFFER)
        message = data.decode().strip()
        
        print(f"Received '{message}' from {address}")
        if state == READY:
            if message == "play":
                secret_number = random.randint(1, 100)
                client_address = address
                attempts = 0
                state = BUSY
                print(f"number to be guessed is {secret_number}")
                server_socket.sendto(b"guess a number between 1 and 100", address)
        elif state == BUSY and address == client_address:
            try:
                guess = int(message)
                attempts += 1
                print(f"client guessed {guess}")
                if guess < secret_number:
                    response = f"the number is > {guess}"
                elif guess > secret_number:
                    response = f"the number is < {guess}"
                else:
                    response = f"guessed after {attempts} attempts"
                    state = READY  # Reset state to READY
                server_socket.sendto(response.encode(), address)
                if state == READY:
                    print("Back to READY state.")
            except ValueError:
                print("Invalid guess. Please enter an integer.")
if __name__ == "__main__":
    main()
