n = int(input("Masukkan angka batas atas( angka >= 2 ): "))

while n<2:
    print("Tidak ada bilangan prima di antara 2 dan angka tersebut, coba masukkan lagi")
    n = int(input("Masukkan angka batas atas( angka >= 2 ): "))
    
print("Bilangan prima antara 2 dan", n, "adalah:")
for i in range(2, n+1):
    u = True
    for j in range(2, i):
        if i % j == 0:
            u = False
            break
    if u:
        print(i, end=" ")   