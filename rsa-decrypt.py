import sys
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
with open("rsa-key.priv","rb") as keyf:
	privatekey=serialization.load_pem_private_key(keyf.read(),password=None)
with open(sys.argv[1],"rb") as encryptedf:
	encryptedData=encryptedf.read()
decrypted=privatekey.decrypt(encryptedData,padding.OAEP(
	mgf=padding.MGF1(algorithm=hashes.SHA256()),
	algorithm=hashes.SHA256(),label=None))
print(decrypted.decode(),end="")
