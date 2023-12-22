import os
os.system('clear')

pendapatan = int(input('pendapatan:'))

if pendapatan <= 1000:
    persentase = 0

elif pendapatan > 1000 and pendapatan <= 2000:
    persentase = 10

elif pendapatan > 2000 and pendapatan <= 3000:
    persentase = 20

elif pendapatan > 3000 and pendapatan <= 4000:
    persentase = 30

elif pendapatan > 4000 and pendapatan <= 5000:
    persentase = 40

else:
    pendapatan >= 5000
    persentase = 50

Bonus = pendapatan* (persentase/100)
Total = pendapatan  + Bonus

print ('pendapatan: ', pendapatan)
print ('persentase: ',persentase)
print ('Bonus: ',Bonus)
print ('Total pendapatan: ',Total)