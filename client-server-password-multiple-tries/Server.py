import socket


def handle_server():
    address = ('127.0.0.1', 2023)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(address)
    server_socket.listen(1)
    print("Server is listening on port 2023")

    client_id = 0
    password = 'abc'
    password_tries = 3

    while True:
        if not continue_connection():
            break

        client_id += 1
        client_socket, client_address = server_socket.accept()
        print(f"Client {client_id} connected")

        if not password_validated(client_socket, password, password_tries):
            continue

        while True:
            message = receive_message(client_socket)
            if message == 'exit':
                handle_exit(client_socket, client_id)
                break

            send_transformed_message(client_socket, message, client_id)

    server_socket.close()


def continue_connection():
    while True:
        continue_input = input(
            'Server is waiting for new clients, continue? Y/N: ')
        if continue_input.lower() == 'y':
            return True
        elif continue_input.lower() == 'n':
            print('Connection refused')
            return False
        else:
            print('Invalid input, please enter Y or N.')


def password_validated(client_socket, password, password_tries):
    password_validated = False

    while not password_validated:
        client_password = client_socket.recv(1024).decode()

        if client_password == password:
            client_socket.send("correct".encode())
            password_validated = True
        else:
            password_tries -= 1

            if password_tries == 0:
                client_socket.send("denied".encode())
                print(f"Client disconnected")
                return False

            client_socket.send('wrong'.encode())

    return True


def receive_message(client_socket):
    return client_socket.recv(1024).decode()


def send_transformed_message(client_socket, message, client_id):
    transformed_message = transform_message(message, client_id)
    client_socket.send(transformed_message.encode())


def transform_message(message, client_id):
    if client_id % 2 == 0:
        return message.upper()
    else:
        return message.lower()


def handle_exit(client_socket, client_id):
    client_socket.close()
    print(f'Client {client_id} disconnected')


handle_server()
