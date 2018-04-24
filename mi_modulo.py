# -*- coding: utf-8 -*-

def crea_listado(listado=[], numElementos=0):
    list=[]

    if numElementos>0:
        print('ENTRA')
        for i in range(len(listado)):
           print('*******: ',listado[i])
           list.append(listado[i])

    return(list)



#crea_listado(['1',2,3],3)