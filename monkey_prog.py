import socket

host = "10.0.0.4"
port = 8095

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print(s.recv(1024).decode("utf-8"))
print(s.recv(1024).decode("utf-8"))

s.send("0".encode('utf-8'))

for i in range(3):
    s.recv(1024)

print(s.recv(1024))