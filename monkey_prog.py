import socket

host = "10.0.0.4"
port = 8095

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print(s.recv(1024).decode("utf-8"))
print(s.recv(1024).decode("utf-8"))

s.send("0\n".encode('utf-8'))

for i in range(6):
    s.recv(1024)



tb = s.recv(1024).decode('utf-8')

print(tb)

print(s.recv(1024))

tb = [[i.replace(" ", "").split("│")] for i in tb.split('\n')]

print(tb)

found = []
to_pop = []
for i in range(len(tb)):
    if i%2 == 0:
        to_pop.append(i)

to_pop.sort(reverse=True)
for n in to_pop:
    tb.pop(n)

print(tb)

for i in range(len(tb)):
    for j in range(len(tb[0])):
        if tb[i][j] != "x" or ' ':
            found.append((tb[i][j], i, j))

found.sort(key=lambda x:x[0])

end_string = ""
for _,x,y in found:
    end_string += str(x) + ',' + str(y) + " "

end_string = end_string[:-1] + "\n"

print(end_string)

s.send(end_string.encode('utf-8'))

print(s.recv(1024))


