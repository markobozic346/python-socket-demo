import socket
import threading


def handle_client(client_socket, client_id):
    print(f"Client with id {client_id} is connected to server")

    client_socket.send(f"Welcome client, your id is {client_id}".encode())

    # receive client messages
    while True:
        message = client_socket.recv(1024).decode()

        if message == 'exit':
            break

        print(f"Client sent you a message: {message}")
        handle_math_expression(message)
        client_socket.send("Message received".encode())

    client_socket.close()
    print(f"Client with id {client_id} is disconnected")


operators = ['+', '/', '*', '-']


def handle_math_expression(exp):
    operator = '+'
    result = 0
    print_expression = ''
    i = 0
    first_iteration = True

    while i < len(exp):
        if exp[i] in operators:
            operator = exp[i]
            print_expression += operator
            i += 1
        else:
            number = ''
            while i < len(exp) and exp[i].isdigit():
                number += exp[i]
                i += 1

            if number:
                number = int(number)
                print_expression += str(number)

                if operator == '+':
                    result += number
                    expression = print_expression + '=' + str(round(result))
                elif operator == '-':
                    result -= number
                    expression = print_expression + '=' + str(round(result))
                elif operator == '*':
                    result *= number
                    expression = print_expression + '=' + str(round(result))
                else:
                    result /= number
                    expression = print_expression + '=' + str(round(result))

                if not first_iteration:
                    print(expression)

                first_iteration = False


def start_server():

    client_id = 0

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    address = ('127.0.0.1', 2023)
    server_socket.bind(address)

    server_socket.listen()
    print("Server is listening on port 2023")

    while True:
        client_socket, client_address = server_socket.accept()

        client_id += 1

        client_thread = threading.Thread(
            target=handle_client, args=(client_socket, client_id))

        client_thread.start()


start_server()
