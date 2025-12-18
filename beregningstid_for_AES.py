import timeit
import matplotlib.pyplot as plt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# AES nøgle og initialiseringsvektor
key = os.urandom(32)  # 256-bit AES nøgle
iv = os.urandom(16)  # 16-byte IV til CBC-mode


# Funktion der krypterer data med AES
def aes_encrypt(data):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad data til 16-byte blokke
    padding_length = 16 - (len(data) % 16)
    padded_data = data + bytes([padding_length] * padding_length)

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext


# Forskellige datastørrelser (i bytes)
data_sizes = [100, 500, 1000, 5000, 10000, 50000]

# Mål krypteringstiden
times = []
for size in data_sizes:
    data = b"AES testbesked" * (size // len(b"AES testbesked"))  # gentag for ønsket størrelse
    t = timeit.timeit(lambda: aes_encrypt(data), number=100)
    times.append(t)

# Plot graf
plt.figure()
plt.plot(data_sizes, times, marker='o')
plt.xlabel("Datastørrelse (bytes)")
plt.ylabel("Tid for 100 krypteringer (sekunder)")
plt.title("AES-krypteringstid vs. datastørrelse")
plt.grid(True)
plt.show()

print("Tider:", times)
