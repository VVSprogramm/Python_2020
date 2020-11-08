'''
Mainīgais String
Ir teksta mainīgais.
a = 'b'
a = "b"
'''

#Teksta izvade, bez mainīgā definēšanas
print('Hello world!', end='\n\n')

#Mainīgo definēšana
var1 = 'Hello'
var2 = "world"

print(var1) #print funkcija pēc noklusējuma tiek sākta jaunā rindā
print(var2)

#Vienā līnijā
#1 veids
print(var1 + ' ' + var2) #izmantojot +, pa vidu jāievieto atstarpe

#2 veids
print(var1 + var2) #Ja atstarpi pa vidu neievieto

#3 veids
print(var1, var2) #Izmantojot komatu, atstarpe tiek ievietota automātiski

#4 veids
print(var1, end=" ") #tiek mainīta end noklusējuma vērtība
print(var2)

#Teksta mainīgā lielums
#Mainīgā lieluma noteikšanai izmanto funkciju len()
print(len(var1)) 

#Piekļuve atsevišķiem mainīgo elementiem
print("var1[0]:", var1[0])
print("var1[1:5]: " + var1[1:5])

#Pēdējais burts
print(var2[-1])

#Viss līdz pēdējam burtam
print(var2[:-1])

#Pārbaude
print(var2)

#Viss ar soli 1
print(var2[::1])

#Viss ar soli 2
print(var2[::2])

#Apgriezt otrādāk
print(var2[::-1])

#Mainīgā maiņa
var1 = var1 + ', ' + "I'm glad to see you"
print(var1)

#Teksta reizināšana
print((var1 + ' ') * 3)

print(var2.upper())
print(var2.lower())
print(var1.split())
print(var1.split('o'))

