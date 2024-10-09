import sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key

with open("rsa-key.priv","rb") as keyf:
	privkey=load_pem_private_key(keyf.read(),password=None)
with open(sys.argv[1],"rb") as f:
	inputdata=f.read()
sig=privkey.sign(
	inputdata,
	padding.PSS(
		mgf=padding.MGF1(hashes.SHA256()),
		salt_length=padding.PSS.MAX_LENGTH
		),
		hashes.SHA256()
	)
with open("myfile.sig","wb") as sigf:
	sigf.write(sig)
