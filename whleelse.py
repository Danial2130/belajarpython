password_benar = "1234"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
        password = input("Masukkan password: ")
        percobaan += 1

        if password == password_benar:
            print("Login berhasil")
            break
        else:
            print(f"Password salah sisa percobaan tersisa {max_percobaan - percobaan}")
else:
    print("Terlalu banyak kesalahan, akses ditolak")