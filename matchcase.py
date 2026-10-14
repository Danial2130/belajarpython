hari = input("Masukkan nama hari: ").lower()


match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat" :
        print("Hari kerja")

    case "sabtu" | "minggu" :
        print("hari libur")
    case _:
        print("Nama hari tidak valid")  