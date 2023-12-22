import os
os.system('clear')

nim = ['2','3','1','0','3','1','0','6','6']

print(nim)

print('item indeks 0 (pertama)',nim[0])
print('item indeks 1 (kedua)',nim[1])

print(f'item indeks 0 (pertama) {nim[0]}')
print(f'item indeks 1 (kedua) {nim[1]}')
print(f'item indeks terakhir {nim[len(nim)-1]}')
print(f'item indeks terakhir {nim[-1]}')
print(f'item indeks (pertama) {nim[-len(nim)]}')

data = ['dwi selsadila', 2023, 'aktif']
        
nilai = [90,89,93,97]

print ('nama: '+ data[0])
print ('angkatan:', data[1])
print ('status: '+ data[2])

# >> Dwi selsadila status Kuliah: Aktif
print(f'{data[0]} status Kuliah: {data[2]}')
# >> Data terbesar nilai adalah: 97
print(f'Data terbesar nilai adalah: {max(nilai)}')
# >> Data terkecil nilai adalah: 89
print(f'Data terkecil nilai adalah: {min(nilai)}')
# >> Rata-rata nilai adalah: 92.25
rataan = sum(nilai)/len(nilai)
print(f'Rata-rata nilai adalah: {rataan}')
# >> Jumlah nilai mahasiswa adalah: 4
print(f'Jumlah nilai {data[0]} adalah: {len(nilai)}')

print (f'{data[0]} ' 'status kuliah:', data [2])

data = (['dwi selsadila', 2023, 'aktif'],
        [79,88,89,98,99],
        [20,22],
        ['S1-Reguler','Ganjil'])

print (data[0][2])
print (data[-1][0])
print (data[2][0:])
print()
matkul = ['matkul kalkulus Dasar',
           'matkul Bahasa Indonesia',
           'matkul Pengantar Pemograman',
           'matkul Sains Terpadu',
           'maktul Agama Islam'] 
sks = [2,3,2,3,3,]
matkul.append(('Pancasila'))
matkul.append(('Pengantar Teknologi Informasi'))
matkul.append(('Wawasan Cinta IPTEK dan IMTAQ'))
print(matkul)
sks.append((2))
sks.append((2))
sks.append((3))
print(sks)
print()

#Daftar mata kuliah
print (f'mata kuliah 1: {matkul[0]} dengan jumlah {sks[0]} sks')
print (f'mata kuliah 2: {matkul[1]} dengan jumlah {sks[1]} sks')
print (f'mata kuliah 3: {matkul[2]} dengan jumlah {sks[2]} sks')
print (f'mata kuliah 4: {matkul[3]} dengan jumlah {sks[3]} sks')
print (f'mata kuliah 5: {matkul[4]} dengan jumlah {sks[4]} sks')
print (f'mata kuliah 6: {matkul[5]} dengan jumlah {sks[5]} sks')
print (f'mata kuliah 7: {matkul[6]} dengan jumlah {sks[6]} sks')
print (f'mata kuliah 8: {matkul[7]} dengan jumlah {sks[7]} sks')
print()
#Nama mahasiswa: Dwi selsadila
print (f'Nama mahasiswa: {data[0][0]}')
#Inisial Dwi selsadila: D s
print (f'Inisial Dwi selsadila: {data[0][0][0]} {data [0][0][4]}')
#Nim Dwi selsadila:231031066
nim_int = int("".join(map(str, nim))) 
print(f"NIM {data[0][0]} : {nim_int}")
#Program Dwi selsadila:S1-reguler sistem informasi b
print (f'Program {data[0][0]} : {data[3][0]} sistem informasi b')
#Angkatan Dwi selsadila: ganjil-2023
print (f'Angkatan {data[0][0]} : {data[3][1]}-{data[0][1]}')
#Total sks Dwi selsadila: 11
print(f'Total sks {data[0][0]} : {len(sks)}')
#Jumlah nilai Dwi selsadila: 5
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])} dan {len(data[2])}')
#Nilai tertinggi Dwi selsadila: 99
print(f'Nilai tertinggi {data[0][0]} adalah: {max(data[1])}')
#Nilai terendah Dwi selsadila: 76
print(f'Nilai terendah {data[0][0]} adalah: {min(data[1])}')
#Rata-rata nilai Dwi selsadila: 92.25
rata = sum(data[1])/len(data[1])
print(f'Rata-rata nilai {data[0][0]} adalah: {rata}')