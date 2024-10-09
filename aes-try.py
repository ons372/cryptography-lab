import sys
import os
from cryptography import *
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
def aesKey():
	return os.urandom(32)
def randomIV():
	return os.urandom(16)
def write(keyfile_name, key, iv):
	with open(keyfile_name, 'wb') as f:
		f.write(key)
		f.write(iv)
def encrypt(inputfile_name, outputfile_name, key, iv):
	backend=default_backend()
	cipher=Cipher(algorithms.AES(key),modes.CBC(iv),backend=backend)
	encryptor=cipher.encryptor()
	pad = padding.PKCS7(algorithms.AES.block_size // 2).padder()
	with open(inputfile_name, 'rb') as infile, open(outputfile_name, 'wb') as outfile:
		while True:
			mes = infile.read(1024)
			if not mes:
				break
			padMes = pad.update(mes)
			encryptMes = encryptor.update(padMes)
			outfile.write(encryptMes)
		padMes = pad.finalize()
		if padMes:
		
			encryptMes=encryptor.update(padMes)+encryptor.finalize()
			outfile.write(encryptMes)
		else:
			encryptMes=encryptor.finalize()
			outfile.write(encryptMes)
inputfile_name=sys.argv[1]
keyfile_name=sys.argv[2]
outputfile_name=sys.argv[3]
key=aesKey()
iv=randomIV()
write(keyfile_name,key,iv)
encrypt(inputfile_name,outputfile_name,key,iv)
