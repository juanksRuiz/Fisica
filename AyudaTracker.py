#-*- coding: utf -8 -*-
def separarDatos(path):
    #Retorna una lista de listas con los valores numericos extraidos de Tracker
    #Primero seleccionar en Tracker los datos COMPLETOS
    #path: direccion del .txt donde estan los datos

    # con indices i se accede/cambia por referencia los valores de una lista

    f = open(path,'r')
    datos = f.readlines()
    datos = datos[2:]
    #print "Datos de entrada:"
    #print datos
    todo = []
    for i in range(len(datos)):
        todo.append(datos[i].split('&'))
    #print "datos string separados"    
    #print todo

    for linea in todo:
        #limpiando lectura de archivo
        if len(linea) != len(todo[0]):
            todo.remove(linea)
        else:
            for i in range(len(linea)):
                if linea[i] == linea[-1]:
                    a = linea[i][:-1]
                    linea[i] = float(a)
                else:
                    linea[i] = float(linea[i])
    #print "Datos de salida"
    #print todo
    #print "Se ha termindo de corregir los datos"
    f.close()
    return todo

def extraerDatos(L,idx):
    #Retorna una lista con los valores del mismo tipo(OJALÁ) de una lista de listas
    #L: lista de listas
    #idx: indice de los datos en cada lista:

    a = []
    for l in L:
        for i in range(len(l)):
            if i == idx:
                a.append(l[i])

    return a
