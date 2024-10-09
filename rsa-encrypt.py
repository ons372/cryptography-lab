import sys
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

with open("rsa-key.pub", "rb") as keyf:
	public = serialization.load_pem_public_key(keyf.read())
with open(sys.argv[1], "rb") as f:
	data = f.read()
encryptdata = public.encrypt(data,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
with open("encrypted.bin", "wb") as encryptedf:
	encryptedf.write(encryptdata)
