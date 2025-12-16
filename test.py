import rsa

# Generer nøgler (x bit)
public_key, private_key = rsa.newkeys(512)

# Besked
message = "HEJSÅ jeg bruger RSA!"

# Krypter med offentlig nøgle
cipher = rsa.encrypt(message.encode(), public_key)

# Dekrypter med privat KEY
plaintext = rsa.decrypt(cipher, private_key).decode()

print("Cipher:", cipher)
print("Decoded:", plaintext)
print(message.encode())
print("Offentlig nøgle",public_key)
print("privat nøgle",private_key)