def ambil_soal():
    soal_asli = []
    with open("bank_soal.txt", "r") as file:
        for line in file:
            soal_asli.append(line.strip())
        return soal_asli
        
soal_asli = ambil_soal()
for soal in soal_asli:
    data= soal.split("|")
    pertanyaan = data[0]
    semua_jawaban = data[1]
    jawaban = semua_jawaban.split(",")
    jawaban_benar = jawaban[0]

    print("Pertanyaan", pertanyaan)
    print("Jawaban", jawaban)
    print("Jawaban benar", jawaban_benar)



