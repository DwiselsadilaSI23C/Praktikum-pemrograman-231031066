import os
os.system('clear')

vd = {'key1' : 'Nilai 1',
      'key2' : 'Nilai 2',
      'key3' : 'Nilai 3'
      }
print(vd)
print(len(vd))
 
#Mengakses Dictionary
print(vd.get('key1'))
print(vd['key1'])

print('\n')

data = {'nama'   : 'Thomas',
        'nim'    : 'B2023001',
        'lulus'  : False
        }
print(data)
#mengakses data
print(data['nama'])
print(data['nim'])
print(data['lulus'])
print()
#mengupdate dan menambah data
# data.update({'nama':'Dwi Selsadila'})
# data['nama'] = 'Dwi Selsadila'
print(data)

# Menghapus data
del data['nim']
print(data)


#Nested Dictionary

kuliah = {'nama'      : 'Dwi Selsadila',
          'nim'       : '231031066',
          'kelas'     : 'si23-c',
          'status'    : 'mahasiswa',
          'alamat'    : 'Gowa',
          'tinggi'    : '160cm',
          'bb'        : '65kg',
          'umur'      : '17th',
          'agama'     : 'Islam',
          'cita-cita' :'Polwan',
          'hobi'      :{'hb1' : 'olahraga',
                        'hb2' : 'menyanyi'
                         }
}
print(kuliah)

print(kuliah['hobi']['hb2'])
print(kuliah['kelas'][1])
print(kuliah['tinggi'])
print(kuliah['bb'])

print(kuliah['hobi'].keys()) 
# melihat seluruh keys


kuliah['hobi']['hb3'] = 'healing'

print(kuliah['hobi'].values()) 
# melihat seluruh nilai/value
# kuliah['hobi'].update({'hb3':'healing'})

print(kuliah)