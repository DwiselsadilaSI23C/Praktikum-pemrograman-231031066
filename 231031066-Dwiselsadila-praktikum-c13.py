import os
os.system('clear')

def fibonacci(n):
    if n < 0:
        print("Tidak ada bilangan yang bernilai negatif")
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

nilai = 20
hasil = fibonacci(20)
print("Finobacci(%d)=%d" % (nilai, hasil))
print()

def fibonacci(n):
    if n < 0:
        print("Tidak ada bilangan yang bernilai negatif")
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

nilai = int(input("masukan sebuah bilangan: "))
hasil = fibonacci(nilai)
print("Finobacci(%d)=%d" % (nilai, hasil))