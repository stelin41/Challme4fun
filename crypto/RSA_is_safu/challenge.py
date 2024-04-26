from Crypto.Util.number import getPrime, bytes_to_long

def cifrar(m):
    done = False
    while not done:
        p = getPrime(256)
        q = getPrime(256)
        e = 3
        n = p*q

        phi = (p-1)*(q-1)
        try:
            d = pow(e, -1, phi)
            done = True
        except ValueError:
            continue

    assert m < n
    assert m**e > n

    print("# Llave publica de Alice:")
    print(f"{e=}")
    print(f"{n=}")

    c = m**e % n

    return c

with open("flag.txt", "r") as f:
    FLAG = f.read().strip()
m = bytes_to_long(FLAG.encode())

# Bob teme que Alice pierda su llave
# ¡Por eso tiene llaves de repuesto!
for i in range(3):
    c = cifrar(m)
    print("# Bob tiene un mensaje para Alice:")
    print(f"{c=}")


