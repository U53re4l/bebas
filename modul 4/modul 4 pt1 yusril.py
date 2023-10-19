def luas_permukaan_kerucut(jari_jari, selimut):
    if jari_jari % 7 == 0:
            luas = 22/7 * jari_jari * (jari_jari + selimut)
    else:
            luas = 3.14 * jari_jari * (jari_jari + selimut)
    return luas

def luas_permukaan_limas_segilima(sisi, alas, tinggi):
    luas_alas = 1.72 * sisi * sisi
    l_sisi_tegak = 5 * (1/2 * alas * tinggi)
    luas = luas_alas + l_sisi_tegak
    return luas

def luas_permukaan_prisma_segilima(alas, tinggi):
    keliling_alas = 5 * alas
    luas_alas = 5 * alas * tinggi
    luas = 2 * luas_alas + (keliling_alas * tinggi)
    return luas

def main():
    print("Program Menghitung Luas Permukaan Bangun Ruang")
    print("1. Kerucut")
    print("2. Limas Segilima")
    print("3. Prisma Segilima")

    pilihan = int(input("Pilih bangun ruang (1/2/3): "))

    if pilihan == 1:
        jari_jari = float(input("Masukkan panjang jari-jari kerucut: "))
        selimut = float(input("Masukkan selimut kerucut: "))
        hasil = luas_permukaan_kerucut(jari_jari, selimut)
        if jari_jari < 0 or selimut < 0:
            print("masukkan bilangan positif")
        else:
            print(f"Luas permukaan kerucut: {hasil:.2f}cm^2")
    elif pilihan == 2:
        sisi = float(input("masukkan sisi limas segilima: "))
        alas = float(input("Masukkan alas limas segilima: "))
        tinggi = float(input("Masukkan tinggi limas segilima: "))
        hasil = luas_permukaan_limas_segilima(sisi, alas, tinggi)
        if sisi < 0 or alas < 0 or tinggi < 0:
            print("masukkan bilangan positif")
        else:
            print(f"Luas permukaan limas segilima: {hasil:.2f}cm^2")
    elif pilihan == 3:
        alas = float(input("Masukkan panjang sisi alas prisma segilima: "))
        tinggi = float(input("Masukkan tinggi prisma segilima: "))
        hasil = luas_permukaan_prisma_segilima(alas, tinggi)
        if alas < 0 or tinggi < 0:
            print("masukkan bilangan positif")
        else:
            print(f"Luas permukaan prisma segilima: {hasil:.2f}cm^2")
    else:
        print("Pilihan tidak valid")

main()