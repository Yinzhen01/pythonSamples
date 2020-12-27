from socket import *

IP = '0.0.0.0'
PORT = 5000
BUFLEN = 512

dataSocket = socket(AF_INET, SOCK_STREAM)

dataSocket.connect((IP, PORT))

while True:
  sendMsg = input('>>')
  if sendMsg == '':
    break

  dataSocket.send(sendMsg.encode())

  receivedMsg = dataSocket.recv(BUFLEN)

  if not receivedMsg:
    break

  print(receivedMsg.decode())

dataSocket.close()
