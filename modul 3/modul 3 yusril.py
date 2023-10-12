angka=int(input("Masukkan size: "))
for i in range (angka):
    for j in range (angka):
        if i==0 or j==0 or i==angka-1 or j==angka-1:
            print("x", end="")
        else:
            print(" ", end="")
    print()

print(end="\n")

for i in range (angka):
    for j in range(angka):
        if i==0 or j==0 or i==angka//2 or i==angka-1 or j==angka-1 and i>angka//2:
            print("x", end="")
        else:
            print(" ", end="")
    print()

print(end="\n")

for i in range (angka):
    for j in range(angka):
        if i==0 or j==0 or i==angka//2 or i==angka-1 or (j==angka-1 and (i>angka//2 and j>angka//2)):
            print("x", end="")
        else:
            print(" ", end="")
    print()

print(end="\n")
