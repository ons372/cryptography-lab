import sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key

with open(sys.argv[1]+".pub","rb") as f:
	publickey=load_pem_public_key(f.read())
with open(sys.argv[2],"rb") as f:
	data=f.read()
with open(sys.argv[3],"rb") as f:
	sig=f.read()
try:
	publickey.verify(
		sig,data,
		padding.PSS(
			mgf=padding.MGF1(hashes.SHA256()),
			salt_length=padding.PSS.MAX_LENGTH),
			hashes.SHA256()
	)
	print("Verified!")
except Exception as e:
	print("Not verified!")
