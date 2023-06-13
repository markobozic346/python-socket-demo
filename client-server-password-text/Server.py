import socket

address = ('127.0.0.1', 2023)

password = 'abc'


def handle_client(server_socket):
    password_correct = False
    while True:

        if not password_correct:
            client_socket, client_address = server_socket.accept()
            print("New client connected")
            client_socket.send('Hello, client!'.encode())

            client_password = client_socket.recv(1024).decode()

            if client_password == password:
                print("Client entered password correctly")
                client_socket.send('correct'.encode())
                password_correct = True

            else:
                print("Client entered password incorrectly")
                client_socket.send('wrong'.encode())
                client_socket.close()

        else:
            message = client_socket.recv(1024).decode()

            if (message == 'exit'):
                print("Client terminated connection")
                client_socket.close()
                password_correct = False

            else:
                client_socket.send(message.upper().encode())


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(address)
    server_socket.listen(1)

    print("Server is listening on port 2023")

    handle_client(server_socket)


start_server()
