ukm_pecintaalam = {"Riki", "Ega", "Nibras", "Jeje", "Mira", "Akbar"}
ukm_bulutangkis = {"Nibras", "Jeje", "Gilang", "Jena", "Ibra", "Ryan"}
ukm_teater = {"Ega", "Angga", "Dika", "Hesti", "Asep"}
ukm_taritradisional = {"Jeje", "Dika", "Budi", "Putri", "Raja", "Sandi"}

#menampilkan mahasiswa lebih dari satu UKM
hasil_ukm = set()
multi_ukm = [ukm_pecintaalam, ukm_bulutangkis , ukm_teater, ukm_taritradisional]
for i in multi_ukm:
    for j in multi_ukm:
        if i == j :
            continue
        else:
            hasil_ukm.update(i&j)
print("==============================================================================")
print(f"Mahasiswa Yang bergabung dalam lebih dari satu UKM adalah{hasil_ukm}")
print("==============================================================================")
print(" ")

#menambah Ibra ke dalam UKM pecinta alam
ukm_pecintaalam.add("Ibra")
print("==============================================================================")
print(f"Ibra Ikut ke dalam UKM bulu tangkis {ukm_pecintaalam}")
print("==============================================================================")
print(" ")

#menghapus Jena dari UKM bulu tangkis 
tidak_ikut_UKM = []
ukm_bulutangkis.remove("Jena")
tidak_ikut_UKM.append("Jena")
print("==============================================================================")
print(f"Jena keluar dari UKM bulu tangkis {ukm_bulutangkis}")
print("==============================================================================")
print(" ")

#mencari ukm dari 4 
ukm_kurangdari_4 = []

ukm_dict = {
    "BULU TANGKIS" : ukm_bulutangkis,
    "PECINTA ALAM" : ukm_pecintaalam,
    "TARI TRADISIONAL" : ukm_taritradisional,
    "TEATER" : ukm_teater
}

for n in ukm_dict:
    if len(n) < 4:
        ukm_kurangdari_4.append(n)

print("==============================================================================")
print("UKM dengan Anggota Kurang Dari 4 :", ukm_kurangdari_4)
print("==============================================================================")
print(" ")

# menampilkan mahasiswa yang tidak ikut UKM
kumpulan_UKM = (ukm_bulutangkis, ukm_pecintaalam, ukm_taritradisional, ukm_teater)
fix_tidakikut = set()
for d in kumpulan_UKM:
    for b in tidak_ikut_UKM:
        if b in d:
            continue
        else :
            fix_tidakikut.add(b)

print("==============================================================================")
print(f"Mahasiswa yang tidak ikut ukm {fix_tidakikut}")
print("==============================================================================")