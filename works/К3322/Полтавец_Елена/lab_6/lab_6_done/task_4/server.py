import socket
from threading import Thread

client_sockets = set()
client_names = {}

def handle_client(client_socket):

    client_name = client_socket.recv(1024).decode()
    client_names[client_socket] = client_name

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                broadcast(f"{client_name}: {message}", client_socket)
            else:
                remove_client(client_socket)
                break
        except:
            remove_client(client_socket)
            break

def broadcast(message, client_socket):
    for client in client_sockets:
        if client != client_socket:
            try:
                client.send(message.encode())
            except:
                remove_client(client)


def remove_client(client_socket):
    if client_socket in client_sockets:
        client_sockets.remove(client_socket)


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8084))
    server.listen(5)
    print("Сервер запущен и ждёт подключения...")

    while True:
        client_socket, address = server.accept()
        print(f"Подключен клиент {address}")
        client_sockets.add(client_socket)
        Thread(target=handle_client, args=(client_socket,)).start()


if __name__ == "__main__":
    main()
