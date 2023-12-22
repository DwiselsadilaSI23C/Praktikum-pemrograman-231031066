import os
os.system('clear')

#input bilangan A
A = int(input('Masukkan bilangan A= '))

#Cek Apakah A adalah kelipatan 4
if A % 4 == 0:
    print(f'{A} adalah bilangan kelipatan 4')
else:
    print(f'{A} adalah bilangaan bukan kelipatan 4')