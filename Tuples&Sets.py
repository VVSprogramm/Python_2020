'''
Mainīgais tuple (slēgtais saraksts)
Nevar mainīt definētos elementus
a = (1,2)
'''

t = (1,2,3)
print(t)

print(t.index(3))

tt = (30,50,60)

print(tt.index(30))
print(tt.index(60))

'''
Mainīgais set (kopa)
Unikālu objektu kopums
s=set(1,2,3)
'''

s=set()
print(s)
s.add(1)
print(s)
s.add('b')
print(s)

l = [1,1,1,2,2,2,3,3,3]
print(set(l))