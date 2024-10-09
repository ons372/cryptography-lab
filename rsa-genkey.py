from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
private = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
with open('rsa-key.priv','wb') as f:
	f.write(private.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption()))
public = private.public_key()
with open('rsa-key.pub','wb') as public_f:
	public_f.write(public.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo))

