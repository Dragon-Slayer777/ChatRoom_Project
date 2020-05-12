import socket
#a socket is basically an endpoint of a communication between two entities so it can send and receive data
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#initializing socket object .socket is a socket subclass , AF_INET refers to IPv4 and sock_stream refers to tcp
s.bind((socket.gethostname(), 1234)) #binds host and port gethostname() gets local ip address of host machine 1234 is a port
s.listen(5)#server program has to listen for connections given to it argument is the queue length incase of multiple connections
while True:
    clientsocket, address = s.accept()#.accept() accepts the clients socket and ip address which is stored in these variables
    print(f"connection from {address} established")# just a string to let us know that connection is established
    clientsocket.send(bytes("Welcome to the server","utf-8"))#sending info to client...,bytes is just encoded data as literal string cannot be sent
    x = clientsocket.recv(1024)
    print(x.decode('utf-8'))