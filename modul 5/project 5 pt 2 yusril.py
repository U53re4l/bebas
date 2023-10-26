dataMahasiswa=[]

while True:
    banyak_mahasiswa = int(input("masukkan berapa banyak data mahasiswa: "))
    if banyak_mahasiswa < 5:
        print("masukkan data minimal 5")
        continue
    else:
        for i in range (banyak_mahasiswa):
            nim = input(f"Masukkan NIM Mahasiswa ke-{i+1}: ")
            nama = input(f"Masukkan Nama Mahasiswa ke-{i+1}: ")
            alamat = input(f"Masukkan Alamat Mahasiswa ke-{i+1}: ")
            prodi = input(f"Masukkan Prodi Mahasiswa ke-{i+1}: ")
            print(" ")
            data=(nim, nama, alamat, prodi)
            dataMahasiswa.append(data)
        break

cariPProdi=input("Masukkan berdasarkan Program Studi berdasarkan data yang ingin dicari: ")

dataMahasiswaDitemukan=[]

for data in dataMahasiswa:
    if cariPProdi.lower() == data[3].lower():
        dataMahasiswaDitemukan.append(data)

if len(dataMahasiswaDitemukan) > 0:
    print("\nData Mahasiswa yang Ditemukan:")
    for data in dataMahasiswaDitemukan:
        print(f"NIM: {data[0]}")
        print(f"Nama: {data[1]}")
        print(f"Alamat: {data[2]}")
        print(f"Program Studi: {data[3]}")
        print("-------------------------")
else:
    print(f"Tidak ditemukan mahasiswa dengan Program Studi: {cariPProdi}")