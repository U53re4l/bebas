while True:
    lama_peminjaman = input("Masukkan lama peminjaman buku (dalam hari): ")

    if not lama_peminjaman.isdigit():
        print("Input tidak valid. Masukkan angka.")
        continue

    lama_peminjaman = int(lama_peminjaman)

    denda_perhari = 2000
    denda_mingguan = 5000

    total_denda = denda_perhari * (lama_peminjaman - 7)

    if lama_peminjaman > 7:
        minggu_lewat = (lama_peminjaman - 7) // 7
        total_denda += denda_mingguan * minggu_lewat
        print(f"Denda yang harus dibayar: Rp{total_denda}")
    else:
        print("tidak ada denda")

    while True:
        ulangi = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ").lower()
        if ulangi in ['ya', 'tidak']:
            break
        else:
            print("Input tidak valid. Masukkan 'ya' atau 'tidak'.")

    if ulangi == 'tidak':
        print("Terima kasih telah menggunakan program.")
        break