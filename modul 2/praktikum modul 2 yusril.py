umur = int(input("masukan umur: "))
if umur > 50:
    print("umur termasuk tua")
elif umur > 25:
    print("umur termasuk dewasa")
elif umur > 17:
    print("umur termasuk muda")
elif umur > 7:
    print("umur termasuk anak anak")
elif umur >= 0:
    print("umur termasuk balita")
else:
    print("umur tidak valid")