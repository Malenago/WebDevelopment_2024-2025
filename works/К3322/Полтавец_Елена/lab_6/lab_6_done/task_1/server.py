import socket

def server_program():
    host = socket.gethostname()
    port = 6321

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Подключение от: " + str(address))

    data = conn.recv(1024).decode()
    print("Письмо от подключенного клиента: " + str(data))

    response = "Hello, client"
    conn.send(response.encode())

    conn.close()

if __name__ == '__main__':
    server_program()

