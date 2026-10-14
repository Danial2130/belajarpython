jml_rendah = 0
jml_sedang = 0
jml_tinggi = 0
total = 0

for i in range(7):
    listrik = int(input(f"Hari ke-{i + 1}: "))

    if listrik < 5:
        jml_rendah += 1
    elif listrik <= 10:
        jml_sedang += 1
    elif listrik > 10:
        jml_tinggi += 1

    total += listrik
    rata = total / 7

print(f"Total Pemakaian: {total} ") 
print(f"Total Pemakaian rendah: {jml_rendah} ") 
print(f"Total Pemakaian sedang: {jml_sedang} ") 
print(f"Total Pemakaian tinggi: {jml_tinggi} ")
print(f"Rata rata pemakaian: {rata}") 
                  