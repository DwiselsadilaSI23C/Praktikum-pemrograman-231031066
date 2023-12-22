print('Nama : Dwi Selsadila')
print('NIM : 231031066')
print('Prodi : Sistem Informasi')
print('Tanggal Lahir : 23-01-2006')

a=66
print('Nilai a =',a)
a=66
a+=1
print('Nilai a+=1 akan menjadi',a)

a=66
print('Nilai a =',a)
a=66
a-=1
print('Nilai a-=1 akan menjadi',a)

a=66
print('Nilai a =',a)
a=66
a*=1
print('Nilai a*=1 akan menjadi',a)

a=66
print('Nilai a =',a)
a=66
a/=1
print('Nilai a/=1 akan menjadi',a)

a=66
print('Nilai a =',a)
a=66
a%=1
print('Nilai a%=1 akan menjadi',a)

a=66
print('Nilai a =',a)
a=66
a**=1
print('Nilai a**=1 akan menjadi',a)

b=True
print('Nilai b =',b)
b|=False
print('Nilai b|=False akan menjadi',b)
b=False
print('Nilai b=',b)
b|=False
print('Nilai b|=False akan menjadi',b)

b=True
print('Nilai b =',b)
b&=False
print('Nilai b&=False akan menjadi',b)
b=False
print('Nilai b=',b)
b&=False
print('Nilai b&=False akan menjadi',b)

b=True
print('Nilai b =',b)
b^=False
print('Nilai b^=False akan menjadi',b)
b=False
print('Nilai b=',b)
b^=False
print('Nilai b^=False akan menjadi',b)

c=0b0100
print('Nilai c =',format(c, '04b'))
c>>=1
print('Nilai c >>=1 akan menjadi',format(c, '04b'))

c=0b0100
print('Nilai c =',format(c, '04b'))
c<<=1
print('Nilai c <<=1 akan menjadi',format(c, '04b'))

a=6
b=11
print('=============== Besar dari 11')
Hasil = a>11
print(a,'> 11 adalah',Hasil)
Hasil = b>11
print(b,'> 11 adalah',Hasil)

print('=============== Besar dari 11')
Hasil = a<11
print(a,'< 11 adalah',Hasil)
Hasil = b<11
print(b,'< 11 adalah',Hasil)

print('=============== Besar atau sama dari 11')
Hasil = a>11
print(a,'> 11 adalah',Hasil)
Hasil = b>11
print(b,'> 11 adalah',Hasil)

print('=============== Besar atau sama dari 11')
Hasil = a<11
print(a,'< 11 adalah',Hasil)
Hasil = b<11
print(b,'< 11 adalah',Hasil)

print('=============== Sama dengan 11')
Hasil = a==11
print(a,'== 11 adalah',Hasil)
Hasil = b==11
print(b,'== 11 adalah',Hasil)

print('=============== Tidak sama dengan 11')
Hasil = a!=11
print(a,'! 11 adalah',Hasil)
Hasil = b!=11
print(b,'! 11 adalah',Hasil)

print('===========NOT===========')
a=True
c = not a
print('a adalah',a)
print('------c = not a-------NOT')
print('c adalah',c)

print('===========OR===========')
a=True
b=True
c=a or b
print(a,'OR',b,'menjadi',c)

a=True
b=False
c=a or b
print(a,'OR',b,'menjadi',c)

a=False
b=True
c=a or b
print(a,'OR',b,'menjadi',c)

a=False
b=False
c=a or b
print(a,'OR',b,'menjadi',c)

print('===========AND===========')
a=True
b=True
c=a and b
print(a,'AND',b,'menjadi',c)

a=True
b=False
c=a and b
print(a,'AND',b,'menjadi',c)

a=False
b=True
c=a and b
print(a,'AND',b,'menjadi',c)

a=False
b=False
c=a and b
print(a,'AND',b,'menjadi',c)

print('===========XOR===========')
a=True
b=True
c=a ^ b
print(a,'^',b,'menjadi',c)

a=True
b=False
c=a ^ b
print(a,'^',b,'menjadi',c)

a=False
b=True
c=a ^ b
print(a,'^',b,'menjadi',c)

a=False
b=False
c=a ^ b
print(a,'^',b,'menjadi',c)

#Tugas
print('===========NAND===========')
a=True
b=True
c= not (a and b)
print(a,'NAND',b,'menjadi',c)

a=True
b=False
c= not (a and b)
print(a,'NAND',b,'menjadi',c)

a=False
b=True
c= not (a and b)
print(a,'NAND',b,'menjadi',c)

a=False
b=False
c= not (a and b)
print(a,'NAND',b,'menjadi',c)

print('===========NOR===========')
a=True
b=True
c= not (a and b)
print(a,'NOR',b,'menjadi',c)

a=True
b=False
c= not (a and b)
print(a,'NOR',b,'menjadi',c)

a=False
b=True
c= not (a and b)
print(a,'NOR',b,'menjadi',c)

a=False
b=False
c= not (a and b)
print(a,'NOR',b,'menjadi',c)

print('===========NXOR===========')
a=True
b=True
c= not (a and b)
print(a,'NXOR',b,'menjadi',c)

a=True
b=False
c= not (a and b)
print(a,'NXOR',b,'menjadi',c)

a=False
b=True
c= not (a and b)
print(a,'NXOR',b,'menjadi',c)

a=False
b=False
c= not (a and b)
print(a,'NXOR',b,'menjadi',c)

print ('=======================IN')
Nama_Lengkap = 'Dwi selsadila'
test = 'a'
cek = test in Nama_Lengkap
print(test+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test = 'rud'
cek = test in Nama_Lengkap
print(test+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test = 'bac'
cek = test in Nama_Lengkap
print(test+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

print ('=======================NOT IN')
Nama_Lengkap = 'Dwi selsadila'
test = 'a'
cek = test not in Nama_Lengkap
print(test+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test = 'rud'
cek = test not in Nama_Lengkap
print(test+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test = 'bac'
cek = test not in Nama_Lengkap
print(test+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

#Tugas
print ('=======================IN')
Nama_Lengkap = 'Dwi selsadila'
test1 = 'dw'
cek = test in Nama_Lengkap
print(test1+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test1 = 'rud'
cek = test in Nama_Lengkap
print(test1+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test1 = 'bac'
cek = test in Nama_Lengkap
print(test1+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

print ('=======================NOT IN')
Nama_Lengkap = 'Dwi selsadila'
test1 = 'dw'
cek = test not in Nama_Lengkap
print(test1+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test1 = 'rud'
cek = test not in Nama_Lengkap
print(test1+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test1 = 'bac'
cek = test not in Nama_Lengkap
print(test1+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

print ('=======================IN')
Nama_Lengkap = 'Dwi selsadila'
test2 = 'wd'
cek = test in Nama_Lengkap
print(test2+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test2 = 'rud'
cek = test in Nama_Lengkap
print(test2+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test2 = 'bac'
cek = test in Nama_Lengkap
print(test2+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

print ('=======================NOT IN')
Nama_Lengkap = 'Dwi selsadila'
test2 = 'wd'
cek = test not in Nama_Lengkap
print(test2+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test2 = 'rud'
cek = test not in Nama_Lengkap
print(test2+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test2 = 'bac'
cek = test not in Nama_Lengkap
print(test2+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

print ('=======================IN')
Nama_Lengkap = 'Dwi selsadila'
test3 = 'a'
cek = test3 in Nama_Lengkap
print(test3+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test3 = 'rud'
cek = test3 in Nama_Lengkap
print(test3+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test3 = 'bac'
cek = test3 in Nama_Lengkap
print(test3+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

print ('=======================NOT IN')
Nama_Lengkap = 'Dwi selsadila'
test3 = 'a'
cek = test3 not in Nama_Lengkap
print(test3+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test3 = 'rud'
cek = test3 not in Nama_Lengkap
print(test3+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test3 = 'bac'
cek = test3 not in Nama_Lengkap
print(test3+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

print ('=======================IN')
Nama_Lengkap = 'Dwi selsadila'
test4 = 'i'
cek = test4 in Nama_Lengkap
print(test4+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test4 = 'rud'
cek = test4 in Nama_Lengkap
print(test4+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test4 = 'bac'
cek = test4 in Nama_Lengkap
print(test4+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

print ('=======================NOT IN')
Nama_Lengkap = 'Dwi selsadila'
test4 = 'i'
cek = test4 not in Nama_Lengkap
print(test4+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test4 = 'rud'
cek = test4 not in Nama_Lengkap
print(test4+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test4 = 'bac'
cek = test4 not in Nama_Lengkap
print(test4+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

print ('=======================IN')
Nama_Lengkap = 'Dwi selsadila'
test5 = 'u'
cek = test5 in Nama_Lengkap
print(test5+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test5 = 'rud'
cek = test5 in Nama_Lengkap
print(test5+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test5 = 'bac'
cek = test5 in Nama_Lengkap
print(test5+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

print ('=======================NOT IN')
Nama_Lengkap = 'Dwi selsadila'
test5 = 'u'
cek = test5 not in Nama_Lengkap
print(test5+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test5 = 'rud'
cek = test5 not in Nama_Lengkap
print(test5+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test5 = 'bac'
cek = test5 not in Nama_Lengkap
print(test5+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

print ('=======================IN')
Nama_Lengkap = 'Dwi selsadila'
test6 = 'e'
cek = test6 in Nama_Lengkap
print(test6+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test6 = 'rud'
cek = test6 in Nama_Lengkap
print(test6+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test6 = 'bac'
cek = test6 in Nama_Lengkap
print(test6+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

print ('=======================NOT IN')
Nama_Lengkap = 'Dwi selsadila'
test6 = 'e'
cek = test6 not in Nama_Lengkap
print(test6+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test6 = 'rud'
cek = test6 not in Nama_Lengkap
print(test6+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test6 = 'bac'
cek = test6 not in Nama_Lengkap
print(test6+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

print ('=======================IN')
Nama_Lengkap = 'Dwi selsadila'
test7 = 'o'
cek = test7 in Nama_Lengkap
print(test7+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test7 = 'rud'
cek = test7 in Nama_Lengkap
print(test7+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test7 = 'bac'
cek = test7 in Nama_Lengkap
print(test7+' terdapat di '+Nama_Lengkap+' adalah '+str(cek))

print ('=======================NOT IN')
Nama_Lengkap = 'Dwi selsadila'
test7 = 'o'
cek = test7 not in Nama_Lengkap
print(test7+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test7 = 'rud'
cek = test7 not in Nama_Lengkap
print(test7+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

test7 = 'bac'
cek = test7 not in Nama_Lengkap
print(test7+' tidak terdapat di '+Nama_Lengkap+' adalah '+str(cek))

a=23
a +=60
b=1
b+= 90
print('=============================AND')
print('Nilai',a,'dalam biner   = ', format(a,'08b'))
print('Nilai',b,'dalam biner   = ', format(b,'08b'))
print('----------------------------(&)')
Hasil=a&b
print('Nilai',a,'&',b,'dalam biner = ', format(Hasil,'08b'))

print('=============================OR')
print('Nilai',a,'dalam biner   = ', format(a,'08b'))
print('Nilai',b,'dalam biner   = ', format(b,'08b'))
print('----------------------------(|)')
Hasil=a|b
print('Nilai',a,'|',b,'dalam biner = ', format(Hasil,'08b'))

print('=============================XOR')
print('Nilai',a,'dalam biner   = ', format(a,'08b'))
print('Nilai',b,'dalam biner   = ', format(b,'08b'))
print('----------------------------(^)')
Hasil=a^b
print('Nilai',a,'^',b,'dalam biner = ', format(Hasil,'08b'))

print('=============================NOT')
print('Nilai',a,'dalam biner   = ', format(a,'08b'))
print('----------------------------(-a)')
Hasil=-a
print('Nilai -',a,'dalam biner = ', format(Hasil,'08b'))

print('Nilai',b,'dalam biner   = ', format(b,'08b'))
print('----------------------------(-b)')
Hasil=-b
print('Nilai -',b,'dalam biner = ', format(Hasil,'08b'))

print('=============================>>')
print('Nilai',a,'dalam biner   = ', format(a,'08b'))
print('----------------------------(>>2)')
Hasil=a>>2
print('Nilai',a,'>>2 dalam biner = ', format(Hasil,'08b'))

print('Nilai',b,'dalam biner   = ', format(b,'08b'))
print('----------------------------(>>2)')
Hasil=b>>2
print('Nilai',b,'>>2 dalam biner = ', format(Hasil,'08b'))

print('=============================<<')
print('Nilai',a,'dalam biner   = ', format(a,'08b'))
print('----------------------------(<<2)')
Hasil=a<<2
print('Nilai',a,'<<2 dalam biner = ', format(Hasil,'08b'))

print('Nilai',b,'dalam biner   = ', format(b,'08b'))
print('----------------------------(<<2)')
Hasil=b<<2
print('Nilai',b,'<<2 dalam biner = ', format(Hasil,'08b'))

#Tugas
print('=============================NOT AND')
print('Nilai',a,'dalam biner   = ', format(a,'08b'))
print('Nilai',b,'dalam biner   = ', format(b,'08b'))
print('----------------------------(&)')
Hasil=a&b
print('Nilai',a,'&',b,'dalam biner = ', format(Hasil,'08b'))

print('=============================NOT OR')
print('Nilai',a,'dalam biner   = ', format(a,'08b'))
print('Nilai',b,'dalam biner   = ', format(b,'08b'))
print('----------------------------(|)')
Hasil=a|b
print('Nilai',a,'|',b,'dalam biner = ', format(Hasil,'08b'))

print('=============================NOT XOR')
print('Nilai',a,'dalam biner   = ', format(a,'08b'))
print('Nilai',b,'dalam biner   = ', format(b,'08b'))
print('----------------------------(^)')
Hasil=a^b
print('Nilai',a,'^',b,'dalam biner = ', format(Hasil,'08b'))

print('=============================NOT (>>2)')
print('Nilai',a,'dalam biner   = ', format(a,'08b'))
print('----------------------------(-a)')
Hasil=-a
print('Nilai -',a,'dalam biner = ', format(Hasil,'08b'))

print('Nilai',b,'dalam biner   = ', format(b,'08b'))
print('----------------------------(-b)')
Hasil=-b
print('Nilai -',b,'dalam biner = ', format(Hasil,'08b'))

print('=============================NOT (>>2)')
print('Nilai',a,'dalam biner   = ', format(a,'08b'))
print('----------------------------(>>2)')
Hasil=a>>2
print('Nilai',a,'>>2 dalam biner = ', format(Hasil,'08b'))

print('Nilai',b,'dalam biner   = ', format(b,'08b'))
print('----------------------------(>>2)')
Hasil=b>>2
print('Nilai',b,'>>2 dalam biner = ', format(Hasil,'08b'))

print('=============================NOT (<<2)')
print('Nilai',a,'dalam biner   = ', format(a,'08b'))
print('----------------------------(<<2)')
Hasil=a<<2
print('Nilai',a,'<<2 dalam biner = ', format(Hasil,'08b'))

print('Nilai',b,'dalam biner   = ', format(b,'08b'))
print('----------------------------(<<2)')
Hasil=b<<2
print('Nilai',b,'<<2 dalam biner = ', format(Hasil,'08b'))
