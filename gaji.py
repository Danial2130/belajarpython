namaKaryawan = input("Masukkan nama karyawan: ")
gajiPokok = float(input("Masukkan jadi pokok: "))
tunjangan = float(input("Masukkan tunjangan: "))

gajiKotor = gajiPokok + tunjangan
potongan = gajiPokok * 0.05
gajiBersih = gajiKotor - potongan

print("Nama Karyawan: ", namaKaryawan)
print("Gaji Kotor: ", gajiKotor)
print("Potongan: ", potongan)
print("Gaji Bersih: ", gajiBersih)

