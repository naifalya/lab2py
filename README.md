# PRAKTIKUM 2: Kondisi If dan Perulangan
Tujuan 
## Kondisi IF
Pada praktikum ini dilakukan pengujian dua latihan, yaitu:
1. 
=======
# PRAKTIKUM 2: Kondisional dan Perulangan

Praktikum ini bertujuan untuk memberikan pemahaman mengenai penerapan struktur kondisi dan perulangan untuk mengatur proses secara otomatis.

## Kondisi IF
1. Latihan 1: Menentukan bilangan terbesar dari sekumpulan bilangan menggunakan _statment if_.

**Digunakan kode pemrograman sebagai berikut:**

```python
print("Masukkan 4 bilangan:")
a = int(input("Bilangan 1: "))
b = int(input("Bilangan 2: "))
c = int(input("Bilangan 3: "))
d = int(input("Bilangan 4: "))

      maks = a

if b > maks:
    maks = b
if c > maks
    maks = c
if d > maks:
    maks = d
    
print("Bilangan terbesar adalah:", maks)
```
**Penjelasan**
  
  Dalam program ini, pengguna diminta untuk memasukkan empat bilangan dengan menggunakan fungsi `input()`, yang selanjutnya dikonversi ke tipe data integer melalui `int()`. Kemudian, variabel maks diinisialisasi dengan bilangan pertama sebagai nilai terbesar sementara. Program selanjutnya menerapkan beberapa kondisi `if` untuk membandingkan bilangan-bilangan berikutnya dengan `maks`. Jika ada bilangan yang lebih besar, maka `maks` akan diganti dengan nilai tersebut. Begitu semua pembandingan telah dilakukan, program akan menampilkan bilangan terbesar yang ditemukan dengan menggunakan `print()`. 

**Hasil latihan 1**
>>>>>>> 13fb6ef3a8e03680cadcea54ecab48afbe2bbd15
