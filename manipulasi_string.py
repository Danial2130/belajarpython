nama = "Danial"
umur = 18

#string tidak bisa di gabung dengan tipe data lain selain string 
#pesan = "Nama saya " + nama + ", umur " + umur
#print(pesan) 

pesan = "Nama saya " + nama + ", umur " + str(umur)
print(pesan)

panjang_nama = len(nama) #len untuk tau jumlah karakter/panjang di str
panjang_pesan = len(pesan) #kalo di js length

print(panjang_nama)
print(panjang_pesan)

#indexing
#karekter di str ada indexnya

nama = "Python"

print(nama[0])
print(nama[1])
print(nama[2])

print(nama[-1])
print(nama[-2])
print(nama[-3])

#slicing

print(nama[0:3])
print(nama[2:5])
print(nama[1:4])


print(nama[:3])
print(nama[2:])
print(nama[:])

#string method(fungsi yang menempel apa tipe data)
#upper huruf besar semua
#lower huruf kecil semua
#titile mengubah setiap awal kata jadi huruf besar
#capitalize setiap awal karakter huruf besar
#strip menghilakan spasi
#replace (dari, menjadi)
#count(text) menghitung berapa kali text
#find(text) mencari posisi

nama = "Danial Maulana"
print(nama)
nama_upper = nama.upper()
print(nama_upper)


nama_lower = nama.lower()
print(nama_lower)


nama_title = nama.title()
print(nama_title)


nama_capitalize = nama.capitalize()
print(nama_capitalize)