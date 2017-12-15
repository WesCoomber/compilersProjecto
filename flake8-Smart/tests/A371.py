#!/usr/bin/python
from Crypto.Cipher import AES
from Crypto import Random

obj = AES.new('Thisisakey123456', AES.MODE_ECB)
message = 'Sample text.....'
ciphertext = obj.encrypt(message)
print ciphertext

BLOCK_SIZE = 16  # Bytes
iv = Random.new().read(AES.block_size)

obj = AES.new('Thisisakey123456', AES.MODE_CBC, iv)
message = 'Sample text.....'
ciphertext = obj.encrypt(message)
print ciphertext
