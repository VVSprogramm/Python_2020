'''
Formatēšanas metodes
'''

#Vecākā formatēšanas metode
print("Mēs te - %s - kaut ko ieliksim" %'kaut kas')
print("Mēs te - %s - kaut ko ieliksim, arī te - %s" %('kaut kas', 'nu, vēl'))

x, y = 'kaut kas', 'nu, vēl'
print("Mēs te - %s - kaut ko ieliksim, arī te - %s" %(x, y))

x, y = 'kaut \tkas', 'nu, vēl'
print("Mēs te - %s - kaut ko ieliksim, arī te - %s" %(x, y))

#Jaunāka metode
print("Teksta ievietošana ar .format metodi: {}" .format ('Hey, Tev izdevās!'))

print('{0} {1}'.format('Hello', 'world'))
print('{1} {0}'.format('Hello', 'world'))
print('{1} {1}'.format('Hello', 'world'))

print('{a} {a}'.format(a='Hello', b='world'))

#f strings, python 3.6+
vards = "Saulcerīte"
print(f"Viņa teica, ka viņas vārds ir {vards}.")
