import socket
import settings


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1",4447))

print("Connected")
#sharing keys

private ,public = settings.keyGenerator()

#sharing keys
r = client.recv(1024)
clientKey = settings.decodeKey(r)
a = public.save_pkcs1(format='DER')
p = settings.EncodeKey(a)
client.sendall(p)


while 1:
    datarecv = client.recv(8192)
    mess = settings.decodeMessage(datarecv)
    message = settings.decryptMessage(mess, private)
    print(f"Friend => {message.decode()}")

    message = input("You => ")
    cipher = settings.encryptMessage(message, clientKey)
    n = settings.EncodeKey(cipher)
    client.sendall(n)
    
    
client.close()