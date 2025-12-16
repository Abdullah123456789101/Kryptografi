import random
import math
import timeit
import matplotlib.pyplot as plt

# Tjek om et tal er primtal (simpel metode)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Generer et primtal med en given bit-længde
def random_prime(bits):
    while True:
        n = random.getrandbits(bits)
        if is_prime(n):
            return n

# Simpel primtalfaktorisering (trial division)
def trial_factor(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i

bit_lengths = [8, 10, 12, 14]
times = []

for bits in bit_lengths:
    p = random_prime(bits)
    q = random_prime(bits)
    n = p * q

    t = timeit.timeit(lambda: trial_factor(n), number=1)
    times.append(t)

plt.figure()
plt.plot(bit_lengths, times, marker='o')
plt.xlabel("Nøglelængde (bits pr. primtal)")
plt.ylabel("Tid til faktorisering (sekunder)")
plt.title("Sammenhæng mellem RSA-nøglelængde og beregningstid")
plt.show()

