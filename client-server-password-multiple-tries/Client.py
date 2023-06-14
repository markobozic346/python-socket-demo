import socket

SERVER_ADDRESS = ('127.0.0.1', 2023)


def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)

    password_validated = False

    while True:
        if not password_validated:
            password_validated = validate_password(client_socket)
            if not password_validated:
                continue

        else:
            client_input = input("Enter a message for the server: ")
            send_message(client_socket, client_input)

            if client_input.lower() == 'exit':
                print('Connection closed')
                client_socket.close()
                break

            server_response = receive_message(client_socket)
            print(f'Server responded with: {server_response}')


def validate_password(client_socket):
    password = input("Enter password: ").encode()
    client_socket.send(password)

    password_response = receive_message(client_socket)

    if 'wrong' in password_response:
        print("Wrong password, try again")
        return False

    if 'denied' in password_response:
        print("Wrong password, connection terminated")
        client_socket.close()
        return False

    return True


def send_message(client_socket, message):
    client_socket.send(message.encode())


def receive_message(client_socket):
    return client_socket.recv(1024).decode()


run_client()
