import socket
sock=socket.socket()
sock.connect(('127.0.0.1',5555))
message = "hi there"
sock.send(message.encode())
data=sock.recv(1024).decode()
print(data)
sock.close()