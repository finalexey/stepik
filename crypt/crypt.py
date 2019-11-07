import simplecrypt

encrypted = open("encrypted.bin", "rb").read()
pwd = open("passwords.txt").readlines()

for p in pwd:
    p = p.strip()
    try:
        decr = simplecrypt.decrypt(data=encrypted, password=p)
    except simplecrypt.DecryptionException:
        continue

    print(decr.decode("utf-8"))
