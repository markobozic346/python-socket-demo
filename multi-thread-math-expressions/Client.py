import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('127.0.0.1', 2023)  # tuple for connection
client_socket.connect(address)

# Initial message for server
init_message = client_socket.recv(1024).decode()
print(init_message)


while True:
    message = input("Input a math expression for server: ")

    client_socket.send(message.encode())

    if message == 'exit':
        break

    server_message = client_socket.recv(1024).decode()
    print(f"Server sent you message: {server_message}")

client_socket.close()
print("Connection terminated")
