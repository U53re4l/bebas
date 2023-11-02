#menampilkan biodata awal
biodata = {
    "nama" : "SUSANTI",
    "alamat" : "SURAKARTA",
    "prodi" : "SISTEM INFORMASI",
    "semester" : 5,
    "angkatan" : 2015 
}

#hasil dari pilihan pengguna
def ubahnama():
    nama = str(input("Masukkan Nama : ")).upper()
    biodata["nama"] = nama

def ubahalamat():
    alamat = str(input("Masukkan Alamat : ")).upper()
    biodata["alamat"] = alamat

def ubahprodi():
    prodi = str(input("Masukkan Prodi : ")).upper()
    biodata["prodi"] = prodi

def ubahsemester():
    semester = int(input("Masukkan Semester : "))
    biodata["semester"] = semester

def ubahangkatan():
    angkatan = int(input("Masukkan Tahun Angkatan : "))
    biodata["angkatan"] = angkatan

ulangi = 1
while ulangi == 1:
    #biodata awal ingin dirubah atau tidak
    print(biodata)
    print(" ")
    print("apakah ingin mengubah data? : ")
    print("1 = iya / 2 = tidak")
    pilihan = int(input("Pilihan anda? : "))
    print(" ")

    #program yang dijalankan setelah hasil pilihan 
    if pilihan == 1:
        ubahnama()
        ubahalamat()
        ubahprodi()
        ubahsemester()
        ubahangkatan()
        print(" ")
        print(biodata)
        print(" ")
        print(" apakah ingin di ulangi? ")
        print(">> 1 = iya | 2 = tidak <<")
        ulangi = int(input("di ulangi atau tidak : "))
        print(" ")
        if ulangi != 1 and ulangi != 2:
            print("Masukkan Sesuai Pilihan Yang Tersedia")
            print(" Apakah ingin di ulangi? ")
            print(">> 1 = Iya | 2 = Tidak <<")
            ulangi = int(input("Di Ulangi atau Tidak : "))
            print(" ")
            if ulangi != 1:
                print("=-=-=-= Program Selesai =-=-=-=")
        else:    
            print("=-=-=-= Program Selesai =-=-=-=")
    elif pilihan == 2:
        print(biodata)
        print(" ")
        print(" apakah ingin di ulangi? ")
        print(">> 1 = iya | 2 = tidak <<")
        ulangi = int(input("di ulangi atau tidak : "))
        print(" ")
        if ulangi != 1:
            print("=-=-=-= Program Selesai =-=-=-=")
    else:
        print("Masukkan Sesuai Pilihan Yang Tersedia")
        print(" Apakah ingin di ulangi? ")
        print(">> 1 = Iya | 2 = Tidak <<")
        ulangi = int(input("Di Ulangi atau Tidak : "))
        print(" ")
        if ulangi != 1:
            print("=-=-=-= Program Selesai =-=-=-=")