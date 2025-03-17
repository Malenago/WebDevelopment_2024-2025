import socket
from threading import Thread
import sys


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("Ошибка соединения. Вы отключены!")
            client_socket.close()
            break


def main():
    host = socket.gethostname()
    server_port = 8084
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, server_port))

    name = input("Введите ваше имя: ")
    client_socket.send(name.encode())

    Thread(target=receive_messages, args=(client_socket,)).start()

    while True:
        message = input()
        if message.lower() == 'Выход':
            client_socket.close()
            sys.exit()
        client_socket.send(message.encode())


if __name__ == "__main__":
    main()
