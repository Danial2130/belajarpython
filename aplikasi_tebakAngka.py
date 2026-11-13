def app_tebak_angka():
    import random
    angka_acak = random.randint(1, 10)
    mask_tebakan = 3
    tebakan = 0
    while tebakan < mask_tebakan:
        tebakan += 1
        angka_user = int(input("Masukkan angka: "))
        if angka_user > angka_acak:
            print("Angka terlalu besar")
        elif angka_user < angka_acak:
            print("Angka terlalu kecil")
        else:
            print("Selamat angka tebakan anda benar")
            break
    else:
        print("Maksimal tebakn sudah habis")
        print("Angka tebakan salah angka yang benar adalah", angka_acak)

    input("Enter untuk lanjut")


def app_menu():
    while True:
        print("Program tebak angka sederhana")
        print("1. Tebak angka")
        print("2. Keluar")
        print("Program tebak angka sederhana")

        pilihan = int(input("Pilihan: "))

        if pilihan == 1:
            app_tebak_angka()
        elif pilihan == 2:
            print("Program tebak angka selesai")
            break
        else:
            print("pilihan tidak valid")


app_menu()