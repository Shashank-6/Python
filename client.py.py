import socket
host=socket.gethostname()
port=5500
s=socket.socket()
s.connect((host,port))
msg=input("->")
while msg!="quit":
    s.send(msg.encode())
    data=s.recv(1024)
    print("Received from server: "+str(data))
    msg=input("->")
s.close()
