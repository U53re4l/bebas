nama = input("masukan nama mahasiswa: ")
tugas = float(input("masukan nilai tugas: "))
uts = float(input("masukan nilai UTS: "))
uas = float(input("masukan nilai UAS: "))
tugas_akhir = float(input("masukan nilai tugas akhir: "))

rata_rata = (tugas + uts + uas + tugas_akhir) /4

print("rata-rata nilai", nama, "adalah", rata_rata)

if 80 <= rata_rata <= 100:
    print("nilai A")
elif 70 <= rata_rata < 80:
    print("nilai B")
elif 60 <= rata_rata < 70:
    print("nilai C")
elif 40 <= rata_rata < 60:
    print("nilai D")
elif 0 <= rata_rata <40:
    print("nilai E")
else:
    print("nilai tidak valid")