import socket

host = "10.0.0.4"
port = 8095

socket.setdefaulttimeout(2)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print(s.recv(1024).decode("utf-8"))
print(s.recv(1024).decode("utf-8"))

s.send("2\n".encode('utf-8'))

for i in range(6):
    s.recv(1024)

print("Start")
tb = s.recv(65536)

for i in range(90):
    a = s.recv(65536)
    tb += a
    if a==b"":
        print("stoping loop")
        break

    print(i)

# try:
#     while True:
#         a = s.recv(2048)
#         if a == b'':
#             raise ValueError("dsbsdub")
#         tb += a
#
# except:
#     tb = tb.decode('utf-8')


tb = tb.decode('utf-8', 'ignore')


tb = tb.replace("\nGive me the path as following:\n  p1|p2|p3|...|pn\nWhere px is a point describe like that:\n  x,y\n>", '')

print(tb)


# │ and |
tb = [i.replace(" ", "│").split("") for i in tb.split('\n')]

print(tb)

found = []
to_pop = []
for i in range(len(tb)):
    if i%2 == 0 or tb[i] == ['']:
        to_pop.append(i)

to_pop.sort(reverse=True)
for n in to_pop:
    tb.pop(n)

print(tb)

for i in range(len(tb)):
    for j in range(len(tb[0])):
        if tb[i][j] != "x" and tb[i][j] != '':
            found.append((tb[i][j], j-1, i))
            print(f"found {tb[i][j]} at x={j}, y={len(tb)-i}")

found.sort(key=lambda x:x[0])

end_string = ""
for _,x,y in found:
    end_string += str(x) + ',' + str(y) + "|"

end_string = end_string[:-1] + "\n"

print(end_string)

s.send(end_string.encode('utf-8'))

print(s.recv(1024))
print(s.recv(1024))


