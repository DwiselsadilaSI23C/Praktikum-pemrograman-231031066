import os
import random as rd
os.system('clear')

warna = ['merah','putih','hitam']
com = rd.choice (warna)
a= True

while a:
    pilih = input ('Masukkan pilihan [merah,putih,hitam]:\n')
    if pilih == com:
        print (f'pilihan anda benar yaitu {pilih}')
        a= False
    else:
        print ('Tebakan anda salah! cba lagi.')

