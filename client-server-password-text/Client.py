import socket


address = ('127.0.0.1', 2023)


def connect_to_server():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(address)

    print('Connected to server')

    return client_socket


def receive_message(client_socket):
    message = client_socket.recv(1024).decode()
    print(f"Server sent you a message:", message)


def send_password(client_socket):
    password = input("Enter password: ")
    client_socket.send(password.encode())
    status = client_socket.recv(1024).decode()
    if status == 'wrong':
        print("Password is wrong")
        return False
    else:
        return True


def start_chat(client_socket):
    while True:
        message = input("Enter a message: ")
        client_socket.send(message.encode())
        if message == 'exit':
            break
        receive_message(client_socket)
    client_socket.close()


# connect to the server
client_socket = connect_to_server()

# receive initial message from server
receive_message(client_socket)

# send password to server
password_correct = send_password(client_socket)

if password_correct:
    start_chat(client_socket)
