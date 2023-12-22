print('PRAKTIKUM 3')

nama = 'dwiselsadila'
nim = '231031066'
meet = 'Praktikum 3 (string)'
prodi = 'Sistem Informasi'
email = 'dwiselsadila@gmail.com'
ttl = 'Sungguminasa, 23-01-2006'
alamat = 'Borong Karamasa'
asal = 'Gowa'
hobi = 'Olahraga'
tinggi = '160'

sp = 40
print('-'*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.lower().rjust(sp))
print('-'*sp)

print(f'''\tHalo ',' nama saya {nama} dengan nim {nim} dari prodi {prodi}, ini adalah file {meet}, terimakasih,\n''')

print(f'''Biodata saya
      
      Nama\t: {nama.upper()}
      NIM\t: {nim}
      Prodi\t: {prodi}
      TTL\t: {ttl}
      Alamat\t: {alamat}
      Asal\t: {asal}
      Hobi\t: {hobi}
      Tinggi\t: {tinggi}cm
         ''')

#Tugas

stat1  = "duFort Frankel Sir Issac"
# Issac duFort Frankel Sir
a      = stat1.split()
stat1 =" ".join( [a[-1],a[0],a[1],a[2]])
print(stat1)
print()


state2 = "duFort Frankel Sir Issac"
a = "duFort Frankel Sir Issac"
# d F S Issac
print  ("duFort"[0], "Frankel"[0], "Sir"[0], "Issac")
print()

stat3 = "duFort Frankel Sir Issac"
# duFort F S I
a = "duFort Frankel Sir Issac"
print ("duFort", "Frankel"[0], "Sir"[0], "Issac"[0])
print()


stat4 = "duFort Frankel Sir Issac"
# I duFort Frankel Sir
a = stat4.split()
stat4 = " ".join([a[-1][0], a[0], a[1], a[2]],)
print(stat4)
print()
                 
stat5 = "duFort Frankel Sir Issac"
# Issac d F S
a  = stat5.split()
stat5 = " ".join([a[-1], a[0][0],a[1][0],a[2][0]])
print(stat5)
print()

stat6 = 'duFort Frankel Sir Issac'
# ISSAC D F S
a = stat6.split()
stat6 = " ".join([a[-1], a[0][0], a[1][0], a[2][0]]).upper()
print(stat6)
print()

stat7 = "#duFort Frankel Sir Issac$"
# duFort Frankel Sir Issac
a = stat7.strip("#,$")
print (a)
print()

stat8 = '#duFort-Frankel-Sir-Issac$'
# duFort Frankel Sir Issac
b = a.strip("#,$")
print(b)
print()
      
stat9 = "#duFort@ ^Frankel* (Sir( (Issac$"
# duFort Frankel Sir Issac
b = a.strip("#,@,$")
print (b)
print()

stat10 = '#duFort@-^Frankel*-(Sir(-(Issac$'
# DUFORT FRANKEL SIR ISSAC
b = a.strip("#,@,$").upper()
print(b)
print()