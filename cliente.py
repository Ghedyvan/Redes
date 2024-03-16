import socket

# Cria o socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8000))

# Loop para enviar e receber mensagens
while True:
  # Envia a mensagem
  mensagem = input('Cliente:')
  client_socket.send(mensagem.encode())
  
  # Recebe a resposta
  data = client_socket.recv(1024)
  print(f"Servidor: {data.decode()}")

# Fecha o socket
client_socket.close()
