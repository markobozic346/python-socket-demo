
# Python socket demo

# Description

The project is a multithreaded Client-Server application for evaluating mathematical expressions. The server side is capable of handling multiple clients simultaneously.

# Features

- The server listens on TCP port X, where X = 2023
- Clients can connect to the LAN IP address of the server.
- The server accepts expressions from clients until 'end' is entered.
- Operators + , -, *, / are supported, with the assumption that all operators have the same priority.
- The server evaluates the expressions and sends intermediate results to the clients.
- The clients receive and display the intermediate results until the initial expression is received.

# Usage

1. Start the server.
2. Connect the clients to the server using the LAN IP address.
3. Enter expressions in the client console.
4. Receive and display the intermediate results.
5. Enter 'end' to stop the evaluation.

# Example

Client input:

80-10+100*3/4

Server output:

80-10=70
80-10+100=170
80-10+1003=510
80-10+1003/4=128
