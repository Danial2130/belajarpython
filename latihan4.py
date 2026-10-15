mahasiswa_lulus = 0
mahasiswa_tidaklulus = 0
total_nilai = 0

for i in range(10):
    nilaimhs = float(input(f"Nilai mahasiswa ke-{i +1}: "))

    if nilaimhs >= 60:
        mahasiswa_lulus += 1
    else:
        mahasiswa_tidaklulus += 1

    total_nilai += nilaimhs

    rata_rata = total_nilai / 10

print(f"Jumalah Mahasiswa Lulus: {mahasiswa_lulus}")
print(f"Jumalah Mahasiswa Tidak Lulus: {mahasiswa_tidaklulus}")
print(f"Total Nilai: {total_nilai}")
print(f"Rata - rata nilai mahasiswa: {rata_rata}")

