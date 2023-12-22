import os
os.system('clear')

a= True
limit = 5
i = 0 

while a:
    i +=1
    print(f'Menjalanka program {limit+1-i}') #cara membalik limit
    if i == limit:
        a= False
        print('program berhenti disini!')
    else:
        a= True
#while a:
#    i =i+1
#   if i <= limit:
#        print('Menjalanka program')
#    a= True
#else:
#    a= False                                                              