import os
os.system('clear')

Nama_karyawan = input('Masukkan nama: ')
pendapatan = int(input('Masukkan Pendapatan: '))

print('Nama',Nama_karyawan)
print('Pendapatan',pendapatan)

if pendapatan >= 1000:
    print('Status: Berhak')
else:
    print('Status: Tidak Berhak')
