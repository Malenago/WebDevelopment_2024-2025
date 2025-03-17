import socket

def client_program():
    host = socket.gethostname()
    port = 6322

    client_socket = socket.socket()
    client_socket.connect((host, port))

    a = input("Введите длину первого катета: ")
    b = input("Введите длину второго катета: ")

    client_socket.send(f"{a} {b}".encode())

    c = client_socket.recv(1024).decode()
    print('Гипотенуза:', c)

    client_socket.close()

if __name__ == '__main__':
    client_program()


