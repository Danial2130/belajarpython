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