def app_penjumlahan():
    print("Program Penjumlahan")
    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 + angka2
    print(f"Hasil penjumlahan, {hasil}")
    print(f"=== Program Penjumlahan Selesai ====")
    input("Enter untuk lanjut")
    print("")
    
def app_pengurangan():
    print("Program Pengurangan")
    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 - angka2
    print(f"Hasil pengurangan, {hasil}")
    print(f"=== Program Penjumlahan Selesai ====")
    input("Enter untuk lanjut")
    print("")

def app_perkaliann():
    print("Program Perkalian")
    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 * angka2
    print(f"Hasil perkalian {hasil}")
    print(f"=== Program Penjumlahan Selesai ====")
    input("Enter untuk lanjut")
    print("")

def app_pembagian():
    print("Program Pembagian")
    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 / angka2
    print(f"Hasil pembagian, {hasil}")
    print(f"=== Program Penjumlahan Selesai ====")
    input("Enter untuk lanjut")
    print("")

def app_menu():
    while True:
        print("Program kalkulator sederhana ")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")
        print("Program kalkulator sederhana ")

        pilihan = int(input("Pilihan: "))

        if pilihan == 1:
            app_perkaliann()
        elif pilihan == 2:
            app_pengurangan()
        elif pilihan == 3:
            app_perkaliann()
        elif pilihan == 4:
            app_pembagian()
        elif pilihan == 5:
            print("Selesai sampai jumpa")
            break
app_menu()