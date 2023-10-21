# A python program that uses AES to encrpyt and decrypt data

# Packages to be imported - pycryptodome
from Crypto.Random import get_random_bytes #used to generate static salt 
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Create a static salt and a password for key generation
salt = b"\xa5\x8c:\xd3\x12\x10\xb7\xc4'\x9aw\x95\nSl\xf2\x10\x04\xb8\x10\x06ZWL\xe1\xa3.,\x17\xd0\x1c\x1f"
password = "MyPassword1234"

# Generate the key
key = PBKDF2(password, salt, dkLen = 32)

# Use the generated key in a cipher to encrypt message
message = b"This message must be hidden!"
cipher = AES.new(key, AES.MODE_CBC) #cipher is created
ciphered_msg = cipher.encrypt(pad(message, AES.block_size)) #message is encrypted

print(ciphered_msg)

# Create a binary file 'encrypted.bin', write ciphered_msg into 'encrypted.bin', not readable
with open('encrypted.bin','wb') as f:
    f.write(cipher.iv) #initialization vector
    f.write(ciphered_msg)

# Open the file to decrypt the cipher
with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_msg = f.read()

# Print the original message in readable form
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
plaintext = unpad(cipher.decrypt(decrypt_msg), AES.block_size)
print(plaintext) 

