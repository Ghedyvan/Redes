import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen()

# clientes = []

def handle_client(client_socket):
  while True:
    data = client_socket.recv(1024)
    print(f"User 1: {data.decode()}")
    mensagem = input('User 2:')
    client_socket.send(mensagem.encode())

while True:

  client_socket, client_address = server_socket.accept()
  #clientes.append(client_socket)
  threading.Thread(target=handle_client, args=(client_socket,)).start()

#for cliente in clientes:
#  cliente.close()
#server_socket.close()
