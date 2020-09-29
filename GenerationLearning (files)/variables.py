first_name = 'Aleix' #string
last_name = 'Pieres' #string

#print(first_name, last_name)  == print(first_name + " " + last_name)

full_name = "Aleix Pieres" #string

print(full_name)

minuscula_nom = 'aleix'

print("Hola Sr." + minuscula_nom.title()) #l'opcio title genera la primera lletra en majuscula

my_book = "My favorite book is 'Elon Musk'" 
print(my_book)
posicio = my_book.find('book')#el que fa trobar es la posicio (int) de la paraula que cercam
print(posicio)

majuscula_nom = 'ALEIX'.lower()#transforma el nom en minuscula

my_book = "My favorite book is 'Elon Musk'".replace('Elon', 'Marc') #l'utilitzam per canviar algunes paraules on tenim un error, molt util per programes molt llargs

my_adress = "   101 Main street    "
print(adress.strip())# strip==tirar\\quitar
print(adress.lstrip())#left strip, JUST LEFT !!
