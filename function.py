def sapa_nama(nama):
    print("Halo", nama)
    print("Senang bertemu dengan anda")

sapa_nama("Danial")
sapa_nama("Fulan")

def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print("Luas persegi panjang adalah: ", luas)

hitung_persegi_panjang(5, 10)

#return value

def hitung_luas_lingkaran(r):
    pi = 3.14159
    luas = pi * r * r
    return luas

luas1 = hitung_luas_lingkaran(7)
luas2 = hitung_luas_lingkaran(10)

print("Luas lingkaran dengan jari-jari 7 adalah: ", luas1)
print("Luas lingkaran dengan jari-jari 10 adalah: ", luas2)

#defult parameter
def sapa(nama, sapaan="Halo"):
    print(sapaan, nama)

sapa("Danial")
sapa("Fulan", "Selamat pagi")

#keyword argument
def perkenalan(nama, umur, kota):
    print("Nama saya", nama)
    print("Umur saya", umur, "tahun")
    print("Saya tinggal di", kota)

perkenalan("Danial", 18, "Jambi") #normal argumen gini harus sesuai urutan parameter

#tapi dengan keyword argument, kita bisa menukar urutan argumen

perkenalan(umur=20, nama="Fulan", kota="Bandung")