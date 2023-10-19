def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def main():
    bilangan = int(input("Masukkan bilangan bulat positif: "))

    if bilangan < 0:
        print("Mohon masukkan bilangan bulat positif.")
    else:
        hasil = faktorial(bilangan)
        print(f"{bilangan}! = {hasil}")

main()