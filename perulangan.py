nama = "Danial Maulana Arshad"

for huruf in nama: #cara perulangan string
    print(huruf)

nama = input("Masukkan nama: ")

for huruf in nama:
    print(huruf)


angka_rahasia = 7

while True:
    tebakan = int(input("Masukkan tebakan: "))
    if tebakan == angka_rahasia:
        print("Angka benar")
        break
    else:
        print("Print salah coba lagi")

