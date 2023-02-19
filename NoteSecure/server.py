import socket

#ConfigServer

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1",4447))

#listening connection

print("server is listing ")
server.listen()
connection , addr = server.accept()
print("Connected")
while 1:
    msg = input("Enter text : ")
    print(f"you : {msg}")
    connection.sendall(msg.encode())

    msgrecv = connection.recv(4096)

    print(f"Friend : {msgrecv.decode()}")




