#1. soal 1
panjang_balok = int(input('panjang balok :'))
lebar_balok = int(input('lebar balok :'))
tinggi_balok = int(input('tinggi balok :'))

volume_balok = panjang_balok*lebar_balok*tinggi_balok

print('panjang balok adalah', panjang_balok, 'cm')
print('lebar balok adalah', lebar_balok, 'cm')
print('tinggi balok adalah', tinggi_balok, 'cm')
print('maka volume balok tersebut adalah', volume_balok, 'cm^3')

#2. soal 2
phi = 3.14
jari_jari_tabung = int(input('jari jari tabung:'))
tinggi_tabung = int(input('tinggi tabung:'))

volume_tabung = phi*jari_jari_tabung**2*tinggi_tabung

print('jari jari tabung adalah', jari_jari_tabung, 'cm' )
print('tinggi tabung adalah', tinggi_tabung, 'cm')
print('maka volume tabung tersebut adalah', volume_tabung, 'cm^3')