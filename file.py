print("Simpan DATA NILAI")

file = open("nilai-siswa.txt", "w")

while True:
    nama = input("Masukkan nama siswa (ketik enter buat selesai): ")
    if nama == "":
        break

    nilai = input("Masukkan nilai siswa: ")

    file.write(nama + "," + nilai + "\n")
    print("Data berhasil disimpan")

file.close()
print("Program selesai")