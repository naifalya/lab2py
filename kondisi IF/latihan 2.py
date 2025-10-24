# Program mengurutkan data dari terkecil ke terbesar

# Meminta jumlah data (minimal 3)
n = int(input("Masukkan jumlah data (minimal 3): "))

if n < 3:
    print("Jumlah data harus minimal 3")
else:
    data = []

    # Input data sejumlah n
    for i in range(n):
        angka = int(input(f"Masukkan bilangan ke-{i + 1}: "))
        data.append(angka)

    # Proses sorting
    data.sort()

    # Tampilkan hasil
    print("Data setelah diurutkan (dari terkecil):", data)
