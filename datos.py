# TUPLAS
print("*************************************************")
print("TUPLAS...............")
print("*************************************************")
tupla=(10,20)
for i in tupla:
    print("Tupla:", i)
for index in range(len(tupla)):
   print('Current tupla(',index,')=', tupla[index])

# LISTAS
print("*************************************************")
print("LISTAS...............")
print("*************************************************")
lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
for i in lista:
    print(i)

# Cargar la lista1 más auto
lista1=[x for x in range(1,51)]
for i in lista1:
    print("Lista1: ", i)
lista1.append(len(lista1)+1)
lista1.append(len(lista1)+1)
for i in lista1:
    print("Lista1: ", i)
lista2=[(x+15) for x in lista1]
for i in lista2:
    print("Lista2: ", i)
for index in range(len(lista2)):
   print('Current lista2[',index,']=', lista2[index])

# DICCIONARIOS
print("*************************************************")
print("DICCIONARIOS...............")
print("*************************************************")
dicc={'Nombre': 'Isabel', 'Direccion': 'Avenida', 'Tno.': '666.66.66.66', 'Email':'ilarrinoa@gmail.com'}
print ("Número elementos del diccionario: ", len(dicc))
for n in dicc:
    print("Diccionario: ", dicc[n])

dicc['Facturacion Total']='1000'
for n in dicc:
    print("Diccionario: ", dicc[n])
for n in dicc.keys():
    print("Index Diccionario[",n,']=', dicc[n])

# CADENA CARACTERES LARGA
print("*************************************************")
print("CADENAS...............")
print("*************************************************")
cadena='loren ipsum ......................'
print("Numero letras de cadena: ", len(cadena))
contador=0
for i in cadena:
    print("Cadena: ", i)
    contador=contador+1
print("Contador: ", contador)
if contador==len(cadena):
   print("Correcto el número de caracteres")
else:
   print("Incorrecto el número de caracteres")
#print("Busqueda dentro de una cadena: ", cadena.find('hola'))
if (cadena.find('ipsum')==-1 and cadena.find('IPSUM')==-1):
    print("La cadena ipsum no está")
else:
    print ("La cadena ipsum está")
## Buscar 'lorem ipsum' con bucle
'''contador=0
contador_letra=0
ipsum='ipsum'
encontrado=False
for letra in cadena:
    if (letra==i) or (letra=='I'):
        contador_letra=1
        petado=False
        while(contador_letra<len(ipsum)):
            if (not(cadena[contador+contador_letra].lower()==ipsum[contador_letra].lower())):
                petado=True
                break
            contador_letra=contador_letra+1
        if (not petado):
            encontrado=True
    contador=contador+1
if (encontrado):
    print ('Encontrado!!!')
else:
    print('No Encontrado!!!')
'''