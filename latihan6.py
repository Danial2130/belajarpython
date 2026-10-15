persen_diskon = 0.10

jml_jenistiket = int(input("Masukkan jumlah jenis tiket (1-15): "))

while jml_jenistiket < 1 or jml_jenistiket > 15:
    print("Jumlah jenis tiket tidak sesuai ketentuan, silakan input kembali")
    jml_jenistiket = int(input("Masukkan jumlah jenis tiket (1-15): "))

# Inisialisasi akumulator dan counter
total_belanja = 0
total_diskon = 0
total_pembayaran = 0
jumlah_diproses = 0

for i in range(jml_jenistiket):
    namafilm = input("Masukkan nama film (STOP untuk berhenti): ")

    if namafilm.upper() == "STOP":
        break

    kategori = input("Masukkan jenis tiket (REGULER/VIP): ")

    while kategori.upper() != "REGULER" and kategori.upper() != "VIP":
        print("Kategori tiket tidak valid, silakan input kembali")
        kategori = input("Masukkan jenis tiket (REGULER/VIP): ")

    harga_tiket = float(input("Masukkan harga tiket (minimal Rp25.000): "))

    while harga_tiket < 25000:
        print("Harga tiket minimal Rp25.000, silakan input kembali")
        harga_tiket = float(input("Masukkan harga tiket (minimal Rp25.000): "))

    jml_tiket = int(input("Masukkan jumlah tiket (1-20): "))

    while jml_tiket < 1 or jml_tiket > 20:
        print("Jumlah tiket tidak valid, silakan input kembali")
        jml_tiket = int(input("Masukkan jumlah tiket (1-20): "))

    # Penyesuaian harga berdasarkan kategori
    if kategori.upper() == "VIP":
        harga_tiket = harga_tiket + 15000
    else:
        harga_tiket = harga_tiket + 0

    # Menghitung subtotal
    subtotal = harga_tiket * jml_tiket

    # Menentukan diskon
    if subtotal > 300000:
        diskon = subtotal * persen_diskon
    else:
        diskon = 0

    # Menghitung total setelah diskon
    total_setelah_diskon = subtotal - diskon

    # Informasi pembelian rombongan
    if jml_tiket > 5:
        print("Pembelian tiket rombongan")

    # Memperbarui akumulator dan counter
    total_belanja += subtotal
    total_diskon += diskon
    total_pembayaran += total_setelah_diskon
    jumlah_diproses += 1

    # Rincian transaksi
    print("\n--- Rincian Tiket ---")
    print(f"Nama film             : {namafilm}")
    print(f"Kategori tiket       : {kategori.upper()}")
    print(f"Harga per tiket      : Rp{harga_tiket:,.0f}")
    print(f"Jumlah tiket         : {jml_tiket}")
    print(f"Subtotal             : Rp{subtotal:,.0f}")
    print(f"Diskon               : Rp{diskon:,.0f}")
    print(f"Total setelah diskon : Rp{total_setelah_diskon:,.0f}")

# Struk akhir setelah perulangan selesai
print("\n========================================")
print("             STRUK PEMBELIAN")
print("========================================")
print(f"Jumlah jenis diproses : {jumlah_diproses}")
print(f"Total belanja         : Rp{total_belanja:,.0f}")
print(f"Total diskon          : Rp{total_diskon:,.0f}")
print(f"Total pembayaran     : Rp{total_pembayaran:,.0f}")
print("========================================")
print("Terima kasih telah membeli tiket!")
