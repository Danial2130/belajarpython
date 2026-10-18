#menyimpan data berpasangan key-value

siswa = {
    "nama": "Danial",
    "umur": 18,
    "kelas": "003"
} 
print(siswa)

print(siswa["nama"])
print(siswa["umur"])
print(siswa["kelas"])

siswa["kelas"] = "004" #edit
print(siswa)

del siswa["umur"] #delete
print(siswa)

for key in siswa:
    print(key, siswa[key])

for key, value in siswa.items():
    print(key, value)