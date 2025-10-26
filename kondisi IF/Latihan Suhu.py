# Program Kontrol Suhu dan Kelembapan

# Deklarasi dan inisialisasi variabel
power = input("Power ON? (y/n): ")

if power.lower() != "y":
    print("Alat Mati")
else:
    # Baca sensor
    suhu = float(input("Masukkan nilai sensor suhu: "))
    kelembapan = float(input("Masukkan nilai sensor kelembapan: "))

    # Batasan suhu dan kelembapan
    S_min = 15
    S_max = 25
    K_min = 45
    K_max = 55

    # Logika kontrol berdasarkan flowchart
    if suhu < S_min:
        print("Pemanas ON, Pendingin OFF")
    elif suhu > S_max:
        print("Pendingin ON, Pemanas OFF")
    elif kelembapan < K_min:
        print("Pengering ON, Pelembab OFF")
    elif kelembapan > K_max:
        print("Pelembab ON, Pengering OFF")
    else:
        print("Semua alat OFF")

    print("Sistem Selesai")
