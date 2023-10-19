def pangkat_dua(bilangan, n=2):
    if n == 0:
        return 1
    else:
        return bilangan * pangkat_dua(bilangan, n-1)

def main(): 
    bilangan = int(input("Masukkan bilangan: "))
    hasil = pangkat_dua(bilangan)
    print(f"{bilangan}^2 = {hasil}")

main()