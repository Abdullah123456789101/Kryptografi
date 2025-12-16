import rsa

puba,priva = rsa.newkeys(1024)
pubb,privb = rsa.newkeys(1024)
# Så Alice's besked bliver : "Hello world". Og det vil hun kryptere til BOB aka BOBBY aka BOBBY71

# Så for at kryptere dem, så er det beskeden, lad os kalde den m opløftet med hans  BOB aka BOBBY aka BOBBY71
#publickey og % hans n, som er det resterende efter at havde divideret tror jeh.
# beskeden er = "Hello World"
mb = "H"
emb = []
def convetominator(mb):
    for i in mb:
        emb.append(ord(i))
convetominator(mb)
t = []
for h in emb:
    a = h ** pubb.e
    b = a % pubb.n
    t.append(b)
#print(t)

# Nu skal bobbydobydi dekryptertorute det. Jeg kan ikke stave klokken er 20:54. Så vi bruger hans private key
u = []
for j in t:
    f = j ** privb.d
    l = f % pubb.n
    u.append(chr(l))
print("Working...")
print("".join(u))