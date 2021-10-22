import hashlib # Importing the hashlib library.

# Encoding the text into bytes and storing it in the variable 'meaasage'.
message = "Hi! This is something to encode".encode()

# The MD5 hash.
print("MD5:", hashlib.md5(message).hexdigest())

# The SHA2 hashes.
print("SHA-256:", hashlib.sha256(message).hexdigest())
print("SHA-512:", hashlib.sha512(message).hexdigest())

# The SHA3 hashes.
print("SHA-3-256:", hashlib.sha3_256(message).hexdigest())
print("SHA-3-512:", hashlib.sha3_512(message).hexdigest())

# 256-bit Blake2 hash.
print("BLAKE2c:", hashlib.blake2s(message).hexdigest())
# 512-bit BLAKE2 hash.
print("BLAKE2b:", hashlib.blake2b(message).hexdigest())
