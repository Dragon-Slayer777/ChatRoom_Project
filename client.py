import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#initializing socket object .socket is a socket subclass , AF_INET refers to IPv4 and sock_stream refers to tcp
s.connect((socket.gethostname(), 1234))#connecting to server, get host name here is just cause both server and client are on the same machine which doesnt happen incase of networks

while True:
    msg = s.recv(1024)# recv: receive data , 1024 is buffer because tcp is just a stream of data 1024 refers to how much of chunks of data youwant to receive at a time
    print(msg.decode("utf-8"))
    x = input("enter message:")
    s.send(bytes(x,"utf-8"))
