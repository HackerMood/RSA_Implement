import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1",4447))
print("Connected")


while 1:
    msgrecv = client.recv(4096)
    print(f"Server : {msgrecv.decode()}")
    msg = input("messge :")
    client.sendall(msg.encode())
    print(f"you : {msg}")

