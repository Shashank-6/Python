import socket
host = ''
port=5500
print(host)
s=socket.socket()
s.bind((host,port))
s.listen(4)
c,addr=s.accept()
print("connection from" +str(addr))
while True:
    data =c.recv(1024)
    if not data:
        break
    print("from connected user:" +str(data))
    data=str(data).upper()
    print("sending : "+str(data))
    c.send(data.encode())
c.close()
