makanan= []

tanya=int(input("Mau berapa makanan yang di input: "))
for i in range (tanya):
    if i >-1:
        food = input(f"Masukkan nama makanan ke-{i+1}: ")
        price = float(input(f"Masukkan harga {food}: "))
        print(" ")
        makanan.append((food, price))
if tanya <0:
    print("Salah")

for food, price in makanan:
    print("Menu Makanan:")
    print(f"{food}: Rp {price:.2f}")