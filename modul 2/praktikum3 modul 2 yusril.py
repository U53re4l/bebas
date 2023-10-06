pilihan = ("batu", "gunting", "kertas")

pemain1 = input("pemain 1 masukkan pilihan (batu/kertas/gunting: )").lower()
while pemain1 not in pilihan:
    print("pilihan tidak sesuai. silahkan masukkan kembali.")
    pemain1 = input("pemain 1 masukkan pilihan (batu/kertas/gunting: )").lower()

pemain2 = input("pemain 2 masukan pilihan (batu/kertas/gunting: )").lower()
while pemain2 not in pilihan:
    print("pilihan tidak sesuai. silahkan masukkan kembali.")
    pemain2 = input("pemain 2 masukkan pilihan (batu/kertas/gunting: )").lower()

if pemain1 == pemain2:
    print("hasilnya seri")
elif (pemain1 == "batu" and pemain2 == "gunting") or \
     (pemain1 == "kertas" and pemain2 == "batu") or \
     (pemain1 == "gunting" and pemain2 == "kertas") :
    print("pemain 1 menang")
else:
    print("pemain 2 menang")