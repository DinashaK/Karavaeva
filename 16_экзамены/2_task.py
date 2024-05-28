# Напишите простой эхо-сервер, использующий неблокирующие сокеты и клиент к нему.
import socket
import selectors

sel = selectors.DefaultSelector()

def handle_connections(server_socket):
    while True:
        events = sel.select()
        for key, mask in events:
            if key.data is None:
                client_socket, client_address = server_socket.accept()
                print(f"Connection from {client_address}")
                client_socket.setblocking(False)
                sel.register(client_socket, selectors.EVENT_READ, client_socket)
            else:
                client_socket = key.data
                data = client_socket.recv(1024)
                if data:
                    print(f"Received: {data.decode()}")
                    client_socket.sendall(data)
                else:
                    sel.unregister(client_socket)
                    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8888))
server_socket.listen(5)
print("Server is listening...")

server_socket.setblocking(False)

sel.register(server_socket, selectors.EVENT_READ, None)

import threading
threading.Thread(target=handle_connections, args=(server_socket,)).start()
