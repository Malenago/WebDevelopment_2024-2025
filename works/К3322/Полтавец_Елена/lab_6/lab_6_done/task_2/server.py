import socket
import math

def server_program():
    host = socket.gethostname()
    port = 6322

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Подключение от: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        a, b = map(float, data.split())
        c = math.sqrt(a**2 + b**2)

        conn.send(str(c).encode())

    conn.close()

if __name__ == '__main__':
    server_program()

