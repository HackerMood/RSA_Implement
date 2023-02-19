import rsa
import base64

def keyGenerator():
    (pubkey, privkey) = rsa.newkeys(512)
    return privkey, pubkey


def encryptMessage(message, publicKey):
    cipher = rsa.encrypt(message.encode(), publicKey)
    return cipher

def decryptMessage(ciphertext, privateKey):
    message = rsa.decrypt(ciphertext, privateKey)
    return message

def EncodeKey(key):
    base64_bytes = base64.b64encode(key)
    return base64_bytes

def decodeKey(key):
    message_bytes = base64.b64decode(key)
    trukey = rsa.key.PublicKey.load_pkcs1(message_bytes, format='DER')
    return trukey

def decodeMessage(key):
    message_bytes = base64.b64decode(key)
    
    return message_bytes

