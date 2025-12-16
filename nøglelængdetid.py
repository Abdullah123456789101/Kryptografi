import timeit
import random
import matplotlib.pyplot as plt

# RSA-nøglelængder i bits

key_lengths = [512, 1024, 2048, 4096]

# Offentlig eksponent (bruges i praksis i RSA)
e = 7
times = []
for bits in key_lengths:
    # Generér et tilfældigt tal n med ønsket bitlængde
    n = random.getrandbits(bits)
    # Tilfældig besked m
    m = random.randint(2, n - 1)
    # Mål tiden for RSA-krypteringens: c = m^e mod n
    t = timeit.timeit(lambda:pow(m, e, n), number=10000)
    times.append(t)
# Lav graf
plt.figure()
plt.plot(key_lengths, times, marker='o')
plt.xlabel("RSA-nøglelængde (bits)")
plt.ylabel("Krypteringstid (sekunder for 100 gentagelser)")
plt.title("Sammenhæng mellem RSA-nøglelængde og krypteringstid")
plt.show()
