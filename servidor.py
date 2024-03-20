import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8400))
server_socket.listen()


def handle_client(client_socket):
  while True:
    data = client_socket.recv(1024)
    print(f"Usuário: {data.decode()}")
    mensagem = input('Servidor: ')
    client_socket.send(mensagem.encode())

while True:

  client_socket, client_address = server_socket.accept()
  threading.Thread(target=handle_client, args=(client_socket,)).start()

server_socket.close()
