import os
import random as rd
os.system('clear')

angka = ['1','2','3','4','5','6','7','8','9','10']
com = rd.choice (angka)
limit = 3
i = 0
a= True

while a:
    i += 1
    pilih = input ('Masukkan pilihan [1,2,3,4,5,6,7,8,9,10]:\n')
    if pilih == com:
        print (f'pilihan kamu benar yaitu {pilih}')
        a= False
    else:
        if i < limit:
            print ('Tebakan kamu salah! Mari coba lagi!')
            print (f'kesempatan kamu tersisa {limit-i} kali:)')
            a=True
        else:
            print ('Gawat Kesempatan kamu habis:)')
            a = False
 
#Tugas: buat program tebak angka 1 sampai 10 dengan batas 
#kesempatan 3 kali, berikan pesan 
# " kesempatan anda tersisa x kali"