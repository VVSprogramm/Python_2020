'''
Mainīgais dictionaries
a = {1:1,2:2,3:3}
'''

#Elementiem var būt dažādi datu tipi
#Teksts
pirmais = {'atsl1':'vertiba1','atsl2':'vertiba2'}
print(pirmais)

#Skaitļi int,float
otrais = {'atsl1':2, 'atsl2':2.5}
print(otrais)

#Lists
tresais = {'atsl1':[1,2,3], 'atsl2':[4,5,6]}
print(tresais)

#Dictionary
ceturtais = {'atsl1':{'atsl2':[2,5,7]}}
print(ceturtais, end = '\n\n')

#Piekļuve elementiem
print(pirmais['atsl1'])
print(otrais['atsl2'])
print(tresais['atsl2'][1])
print(ceturtais['atsl1']['atsl2'][2], end = '\n\n')

#
otrais['atsl1'] = otrais ['atsl1'] - 2
print(otrais['atsl1'])

#
otrais['atsl1'] -=  4
print(otrais['atsl1'], end = '\n\n')

#Tukšas dictionary radīšana
d = {}
d['atsl1'] = 'Kā iet?'
d['atsl2'] = 'Man labi, kā tev?'

print(d)
print(d['atsl1'], end = '\n\n')

#Parādīt visas atslēgas
print(pirmais.keys())

#Parādīt visus elementus
print(pirmais.values())

#Parādīt tuples
print(pirmais.items(), end = '\n\n')