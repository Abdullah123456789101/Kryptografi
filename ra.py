p = 17
q = 19
e = 3
m = 66

#beregning af n
n = p*q

#beregning af phi
phi = (p-1)*(q-1)

#beregning af d
d = pow(e,-1,phi)

#kryptering
c = pow(m,e,n)
print(c)

#dekryptering
print(pow(c,d,n))