from socket import *

IP = '0.0.0.0'
PORT = 5000
BUFLEN = 512

listenSocket = socket(AF_INET, SOCK_STREAM)

listenSocket.bind((IP, PORT))

listenSocket.listen(5)
print(f'server start, waiting for port {PORT}...')

dataSocket, addr = listenSocket.accept()
print('Connection establishment...')

while True:
  receivedMsg = dataSocket.recv(BUFLEN)

  if not receivedMsg:
    break
  
  message = receivedMsg.decode()
  print(f'receive message: {message}')

  dataSocket.send(f'message {message} have been received by server'.encode())

dataSocket.close()
listenSocket.close()
