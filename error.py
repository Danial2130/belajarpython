#print("Hello, World  sytanx error

#Name error, tidak ada variabel nama

#print(nama)

#print("6" + 6) #Type error, tidak bisa menambahkan string dengan integer


#value error, tidak bisa mengubah string menjadi integer

#value = int("abc")


#index error, tidak bisa mengakses index ke 5 karena hanya ada 3 index

#list = [1, 2, 3]
#print(list[5])

#Key error, tidak ada key "alamat" di dictionary
#dict = {"nama": "John", "umur": 30}
#print(dict["alamat"])

#ZeroDivisionError
#print(10 / 0)


#penangan error dengan try except
# print("Kalkulator Sederhana")


# try:
#     angka1 = int(input("angka pertama: "))
#     angka2 = int(input("angka kedua: "))
#     hasil = angka1 / angka2
#     print("Hasil pembagian: ", hasil)

# except ValueError:
#     print("Input harus berupa angka")#error khusus value error
# except ZeroDivisionError:
#     print("Tidak bisa membagi dengan nol")
# except:
#     print("Terjadi kesalahan di input pengguna")

# print("Program selesai")

#error secara general


#try except else
try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input harus berupa angka")
else:
    print("Angka yang dimasukkan adalah: ", angka)
    if angka < 0:
        print("Angka negatif")
    elif angka > 0:
        print("Angka positif")
    else:print("Angka nol")
finally:
    print("Program selesai")#di jalankan walaupun terjadi error atau tidak