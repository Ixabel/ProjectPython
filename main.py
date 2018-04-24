
lista1=[x for x in range(1,51)]
lista2=[(x+15) for x in lista1]

# Definicion de una FUNCION **************
def cuenta(listado):
    for elemento in listado:
        print ('Elemento de un listado por funcion: ', elemento)

def divide(D=4,d=2):
    print(D/d)

# Invocacion a una FUNCION **************
print('******************FUNCION Cuenta*******************************')
cuenta(lista2)
print('***************************************************************')

print('******************FUNCION Divide*******************************')
divide()
divide(6)
divide(d=6)
divide(5,3)
divide(d=5,D=3)
print('***************************************************************')


print('******************FUNCION Leer Fichero CSV*******************************')

def recorrer_fichero(fichero):
    fichero_csv = open(fichero)
    correcto = True
    numero_lineas_correctas = 0
    contador_elementos_bueno = 0
    for line in fichero_csv:
        #Contar el numero de elementos correcto de la primera linea
        if (numero_lineas_correctas==0):
            contador_elementos_buenos=line.count(',')+1
            print('CONTADOR ELEMENTOS BUENOS DE LA PRIMERA LINEA: ', contador_elementos_buenos)
            numero_lineas_correctas = numero_lineas_correctas + 1
        #print('NUMERO ELEMENTOS BUENO PRIMERA LINEA: ',contador_elementos_bueno)
        #print (line.rstrip())
        else:
            if (contador_elementos_buenos==line.count(',')+1):
                numero_lineas_correctas=numero_lineas_correctas+1

    fichero_csv.close()
    return numero_lineas_correctas


numero_total=recorrer_fichero("sonar.all-data.csv")
#numero_total=recorrer_fichero("fichero_vacio.csv")
if (numero_total == 0):
    print('El Fichero está vacío: ', numero_total)
else:
    print('Numero TOTAL de LINEAS CORRECTAS del fichero: ', numero_total)

print('*************************************************************************')

