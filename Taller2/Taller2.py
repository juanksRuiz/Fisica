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
    #path: direccion del .txt donde estan los datos

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

def metodoEuler(h,listaInput,listaIntegral):
    #Metodo que calcula la integral de una lista de valores
    #h: paso de los valores
    #listaInput: lista cuyos valores se van a integrar
    #listaIntegral: lista de valores obtenidos al integrar (NOTA: Comienza con su valor inicial)
    for i in range(len(listaInput)-1):
        ival = listaIntegral[i] + h*listaInput[i]
        listaIntegral.append(ival)
         
    return listaIntegral

#######################################
#Salto de Felipe (ligera flexion)
mf = 64.0 #kg
pf = 'C:\Users\juank\Desktop\datosFelipe.txt'
datosFelipe = separarDatos(pf) #tiempo /v(m/s) / a(m/s^2)
accelAntes = [] #los i <= 6
accelDesp = [] #los i>6
for i in range(len(datosFelipe)):
    if i <= 6:
        accelAntes.append(datosFelipe[i][2])
    else:
        accelDesp.append(datosFelipe[i][2])

print "aceleracion antes:"
print accelAntes
print "acceleracion depues:"
print accelDesp

f1_antes = promedio(accelAntes)*mf
print "Fuerza prom. antes: ",f1_antes

f1_despues = promedio(accelDesp)*mf
print "Fuerza prom. despues: ",f1_despues

#Para Andres (flexion amplia)
ma = 81 #kg
pa = 'C:\Users\juank\Desktop\datosAndres.txt'
datosAndres = separarDatos(pa)
accAntes = []
accDesp = []

