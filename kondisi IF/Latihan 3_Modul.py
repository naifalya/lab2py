# Program Pemesanan Tiket Bioskop
print("=== Pemesanan Tiket Bioskop ===")
print("1. Reguler (Rp50.000)")
print("2. VIP     (Rp100.000)")

tipe = input("Pilih tipe tiket (1/2): ")
member = input("Apakah Anda memiliki kartu member? (y/n): ")

# Menentukan harga berdasarkan pilihan tiket
if tipe == "1":
    harga = 50000
elif tipe == "2":
    harga = 100000
else:
    print("Pilihan tidak valid")
    exit()

# Ternary operator untuk diskon
diskon = 0.2 * harga if member.lower() == "y" else 0

total = harga - diskon

print("---------------------------------")
print("Harga tiket      : Rp", harga)
print("Diskon           : Rp", int(diskon))
print("Total bayar      : Rp", int(total))
