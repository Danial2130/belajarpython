x = 17
y = 17
hasil = (x > y) or (x >= y) and (x != y)

print(hasil)

jumlah = 0
for angka in range(2, 9):
    if angka % 3 == 0:
        continue
    jumlah += angka
print(jumlah)