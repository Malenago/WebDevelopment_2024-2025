import socket

def client_program():
    host = socket.gethostname()
    port = 6321

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = "Hello, server"
    client_socket.send(message.encode())

    data = client_socket.recv(1024).decode()
    print('Получено от сервера: ' + data)

    client_socket.close()

if __name__ == '__main__':
    client_program()

