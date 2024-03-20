import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8400))

while True:
  mensagem = input('Usuário: ')
  client_socket.send(mensagem.encode())
  data = client_socket.recv(1024)
  print(f"Servidor: {data.decode()}")

client_socket.close()
