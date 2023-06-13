# Project Name: Client-Server Application

## Description
This project is a simple client-server application implemented in the Python language. The client connects to the server by entering the corresponding password. If the password is incorrect, the client receives an appropriate message, and the connection is terminated. If the password is correct, the client receives an appropriate message, and the communication continues. The client enters a message from the keyboard, and the server returns the client's message in uppercase (example: "hello" -> "HELLO"). The communication continues until the client enters "exit". The server remains listening and, if possible, accepts new clients.

## Features

### 1. Password Validation
- The client can connect to the server by entering a password.
- If the entered password is incorrect, the client receives an error message and the connection is terminated.
- If the entered password is correct, the client receives a success message, and the communication continues.

### 2. Message Exchange
- The client can enter a message from the keyboard.
- The server receives the client's message and returns it in uppercase.
- Example: "hello" -> "HELLO".

### 3. Continuous Communication
- The communication between the client and server continues until the client enters "exit".
- The server remains listening for client messages.
- The server can accept new clients while maintaining the connection with the existing client.
