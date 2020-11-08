'''
Mainīgais list (saraksts)
Elementi var tikt mainīti
a = [1,2,3]
'''

#Definē ar []
my_list = [1,2,3]
print(my_list, end = '\n\n')

#Var saturēt gan ciparus, gan tekstu
your_list = ['Teksts', 15, 16.5]
print(your_list, end = '\n\n')

#Var izmantot len funkciju, lai noteiktu elementu skaitu sarakstā
print("my_list:",len(my_list))
print("your_list:",len(your_list), end = '\n\n')

#Var izmantot index
print(my_list[0])
print(my_list[0:])
print(my_list[:1], end = '\n\n')

#Elementa maiņa
my_list[0] = 'Sveiki'
print(my_list, end = '\n\n')

#Var pievienot ar +
print(my_list + ["Redzēji?"])
#Lai saglabātu izmaiņas, nepieciešams pārdēvēt
my_list = my_list + ["Redzēji?"]
print(my_list)
print('Jaunais garums:',len(my_list), end = '\n\n')

#Var izmantot *
print(my_list *2, end = '\n\n')

#Append
your_list.append('append me!')
print(your_list, end = '\n\n')

#Pop off
your_list.pop(0)
print(your_list, end = '\n\n')

#Pop elementa parādīšana
popped_item = your_list.pop()
print(popped_item)

print(your_list, end = '\n\n')
