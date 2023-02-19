import socket
import settings

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server.bind(("127.0.0.1",4447))

server.listen()
print("Server is listning")
connection , addr = server.accept()

#getting All (Priv | pub) keys

private ,public = settings.keyGenerator()

#sharing keys

a = public.save_pkcs1(format='DER')
p = settings.EncodeKey(a)
connection.sendall(p)
r = connection.recv(1024)
clientKey = settings.decodeKey(r)

while 1:
    message = input("You =>  ")
    cipher = settings.encryptMessage(message, clientKey)
    n = settings.EncodeKey(cipher)
    connection.sendall(n)

    datarecv = connection.recv(8192)
    mess = settings.decodeMessage(datarecv)
    message = settings.decryptMessage(mess, private)
    print(f"Friend => {message.decode()}")

connection.close()