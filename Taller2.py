#p = 'C:\Users\juank\Desktop\lectura.txt'

def promedio(valores):
    #Retorna el promedio de los valores ingresados
    suma = 0
    for v in valores:
        suma = suma + float(v)
    return suma/(len(valores))

def sd(valores):
    #Retorna la desviacion estandar de los valores ingresados
    mean = promedio(valores)
    sumDist = 0
    for v in valores:
        sumDist = sumDist + (v-mean)**2

    sd = sumDist**(1.0/2.0)
    return sd

def separarDatos(path):
    #Retorna una lista de listas con los valores numericos extraidos de Tracker
    #Primero seleccionar en Tracker los datos COMPLETOS
    #parh: direccion del .txt donde estan los datos

    f = open(path,'r')
    datos = f.readlines()
    datos = datos[2:]
    todo = []
    for i in range(len(datos)):
        todo.append(datos[i].split('&'))

    for linea in todo:
        for i in range(len(linea)):
            if linea[i] == linea[-1]:
                linea[i] = float(linea[i].replace('\n',''))
            else:
                linea[i] = float(linea[i])
    f.close()
    return todo
