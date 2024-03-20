import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

while True:
  mensagem = input('User 1:')
  client_socket.send(mensagem.encode())
  data = client_socket.recv(1024)
  print(f"User 2: {data.decode()}")

client_socket.close()
