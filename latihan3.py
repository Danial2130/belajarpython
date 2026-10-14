total_belanja = 0
diskon = 10000

for i in range(5):
    harga_barang = float(input(f"Harga barang ke-{i + 1}: "))
    total_belanja += harga_barang
    if total_belanja >= 100000:
        total_pembayaran = total_belanja - diskon
    else:
        total_belanja + 0
print(f"Total belanja   : Rp{total_belanja}")
print(f"Dison           : Rp{diskon}")
print(f"Total pembayaran: Rp{total_pembayaran}")