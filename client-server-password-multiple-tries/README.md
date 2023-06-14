# Client-Server Password multiple tries

This is a client-server application that follows the specified requirements:

## Client

- Upon connection, the client enters the correct password (3 attempts).
  - If it is incorrect, the client receives an appropriate message:
    - After the first two incorrect attempts: "Try again."
    - After the third incorrect attempt: "Invalid password." The connection is then terminated.
  - If it is correct, the client receives a confirmation message, and the communication continues.

- The client enters a message from the keyboard and sends it to the server for processing.
  - If the client's serial number is even, the server returns the message in uppercase.
  - If the client's serial number is odd, the server returns the message in lowercase.

- The communication between the client and the server continues until the client enters "exit".

## Server

- The server listens for incoming connections and optionally accepts new clients.
  - Before each `accept`, the server receives the question "Continue? Y/n" from the keyboard.
  - If the input is "Y", the server waits for new clients.
  - If the input is "n", the server shuts down.