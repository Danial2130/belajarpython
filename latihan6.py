jml_jenistiket = int(input("Masukkan jumlah jenis tiket (1-15): "))

while jml_jenistiket < 1 or jml_jenistiket > 15:
    print("Jumlah tiket tidak sesuai ketentuan silahkan input kembali")
    jml_jenistiket = int(input("Masukkan jumlah jenis tiket (1-15): "))

for i in range(jml_jenistiket):
    namafilm = input("Masukkan nama film (stop untuk berhenti )")