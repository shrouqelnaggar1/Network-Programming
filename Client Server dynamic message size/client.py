import socket

clsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("client socket created")

# hostName=socket.gethostname() 
hostName="127.0.0.1"
port=5524

clsocket.connect((hostName,port))

recievedMess=clsocket.recv(1024).decode('utf-8')
print(f"server send [ {recievedMess} ] to you")

client_message = input("as client :) Enter your message: ")
clsocket.send(client_message.encode('utf-8'))

# If the message length is greater than 1024 bytes, send it in chunks
if len(client_message) > 1024:
    chunk_size = 1024
    for i in range(0, len(client_message), chunk_size):
        clsocket.send(client_message[i:i+chunk_size])#.encode('utf-8'))
else:
    clsocket.send(client_message.encode('utf-8'))

clsocket.close()