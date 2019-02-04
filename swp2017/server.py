import sys, socket

IP = "127.0.0.1"
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))

print("Start listen")
s.listen(1)
csocket, address = s.accept()

print(address)

while True:
    data = csocket.recv(1024)
    print(data.decode())

s.close()