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


# print("Menampilkan DATA NILAI")

# file = open("nilai-siswa.txt", "r")

# for line in file:
#     data = line.strip().split(",")
#     print(data[0] + " memiliki nilai " + data[1])

# file.close()
# print("Program selesai")


#With statement memastikan file otomatis tertutup bahkan jika terjadi error

# print("Menampilkan DATA NILAI")

# with open("nilai-siswa.txt", "r") as file:
#     for line in file:
#         data = line.strip().split(",")
#         print(data[0] + " memiliki nilai " + data[1])


# print("Program selesai")
#tidak perlu clode karena sudah di tutup otomatis oleh with

#error handling
#walaupun sudah menutup file menggunakan with state ment tapi jka error maka aplikasi tetapi berhenti
#menggunakan try except

print("Menampilkan DATA NILAI")

try:
    with open("nilai-siswa.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            print(data[0] + " memiliki nilai " + data[1])
except FileNotFoundError:
    print("File tidak di temukan")

print("Program selesai")