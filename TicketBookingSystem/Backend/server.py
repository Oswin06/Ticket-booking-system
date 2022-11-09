import socket
sock=socket.socket()
sock.bind(('127.0.0.1',5555))
sock.listen(1)
conn,addr= sock.accept()
flag=1
while flag==1:
    data=conn.recv(1024).decode()
    print(data)
    if not data:
        flag=0
        print(data)
    conn.send(data.encode())
conn.close()