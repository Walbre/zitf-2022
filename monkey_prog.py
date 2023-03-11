import socket

host = "10.0.0.4"
port = 8095

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print(s.recv(1024))