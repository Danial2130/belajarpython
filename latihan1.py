namaPengguna = input("Masukkan Nama Pengguna: ")
skorA = int(input("Masukkan Penjualan Produk A"))
skorB = int(input("Masukkan Penjualan Produk B"))
skorKepuasan = int(input("Masukkan Skor Kepuasan"))

skorAkhir = (0.25 * skorA) + (0.35 * skorB) + (0.40 * skorKepuasan)

print(f"Skor akhir {skorAkhir}")