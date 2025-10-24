print("Masukkan 4 bilangan:")
a = int(input("Bilangan 1: "))
b = int(input("Bilangan 2: "))
c = int(input("Bilangan 3: "))
d = int(input("Bilangan 4: "))

maks = a

if b > maks:
    maks = b
if c > maks:
    maks = c
if d > maks:
    maks = d

print("Bilangan terbesar adalah:", maks)
