import sys, socket


IP = "127.0.0.1"
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((IP, PORT))

msg = "hello"
s.sendall(msg.encode())

s.connect()