import socket
import threading

# Cria o socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))
server_socket.listen(1)

# Lista de clientes conectados
clientes = []

# Função para tratar cada cliente
def handle_client(client_socket):
  while True:
    # Recebe a mensagem do cliente
    data = client_socket.recv(1024)
    
    # Exibe a mensagem do cliente
    print(f"Cliente: {data.decode()}")
    
    # Envia uma resposta ao cliente
    mensagem = input('Servidor:')
    client_socket.send(mensagem.encode())

# Loop para aceitar novas conexões
while True:
  # Aceita uma conexão
  client_socket, client_address = server_socket.accept()
  
  # Adiciona o novo cliente à lista
  clientes.append(client_socket)
  
  # Cria uma thread para tratar o novo cliente
  threading.Thread(target=handle_client, args=(client_socket,)).start()

# Fecha os sockets
for cliente in clientes:
  cliente.close()
server_socket.close()
