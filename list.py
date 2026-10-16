daftar_kosong = []
print(daftar_kosong)

angka = [1, 2, 3, 4, 5, 6]
print(angka)

nama = ["Danial", "fulan", "fulanah"]
print(nama)

campuran = ["Danial", 90, "Budi", 80 ]
print(campuran)


buah = ["apel", "jeruk", "mangga"]
print(buah[0])
print(buah[1])
print(buah[2])

warna = ["merah", "ijo", "ungu"]
print(warna)
warna[1] = "kuning"
print(warna)


makanan = ["nasi goreng", "bakso"]
print(makanan)
makanan.append("Soto")
print(makanan)
makanan.insert(1, "Mie ayam")
print(makanan)

makanan.remove("nasi goreng")
print(makanan)

makanan.pop()
print(makanan)

del makanan[0]
print(makanan)

jus = ["alpukat", "jeruk", "mangga"]
print(len(jus))

satu = [1, 2, 3, 4, 5]
print(satu)
dua = [6, 7, 8, 9, 10]
print(dua)

gabung = satu + dua
print(gabung)


alat_tulis = ["pena", "pensil", "spidol", "penggaris"]
for atk in alat_tulis:
    print(atk)

for i in range(0, len(alat_tulis)):
    print(alat_tulis[i])

if "pena" in alat_tulis:
    print("ada pena")
else:
    print("tidak ada pena")