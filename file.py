# print("Simpan DATA NILAI")

# file = open("nilai-siswa.txt", "w")

# while True:
#     nama = input("Masukkan nama siswa (ketik enter buat selesai): ")
#     if nama == "":
#         break

#     nilai = input("Masukkan nilai siswa: ")

#     file.write(nama + "," + nilai + "\n")
#     print("Data berhasil disimpan")

# file.close()
# print("Program selesai")


print("Menampilkan DATA NILAI")

file = open("nilai-siswa.txt", "r")

for line in file:
    data = line.strip().split(",")
    print(data[0] + " memiliki nilai " + data[1])

file.close()
print("Program selesai")