# -*- coding: utf: -8 -*-
print "Importando paquetes..."
import numpy as np
import matplotlib.pyplot as plt
print "Listo !"
#los videos son el 9(Andres - GRAN flexion) y el 16 (Felipe - POCA flexion)
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


def separarDatos(path):
    #Retorna una lista de listas con los valores numericos extraidos de Tracker
    #Primero seleccionar en Tracker los datos COMPLETOS
    #path: direccion del .txt donde estan los datos
<<<<<<< HEAD

    # con indices i se accede/cambia por referencia los valores de una lista
=======
>>>>>>> 1f42b4baf588fc587602f812790b19ddb2996795

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
pf = 'C:\Users\juank\Desktop\Fisica\Taller2\datosFelipe.txt'
datosFelipe = separarDatos(pf) #tiempo /v(m/s) / a(m/s^2)
accelAntes = [] #los i <= 6
accelDesp = [] #los i>6
for i in range(len(datosFelipe)):
    if i <= 6:
        accelAntes.append(datosFelipe[i][1])
    else:
        accelDesp.append(datosFelipe[i][1])

#Punto 8
f1_antes = promedio(accelAntes)*mf
print "Datos de Felipe - POCA FLEXION"
print "Fuerza prom. antes: " + str(f1_antes) + ' N'

f1_despues = promedio(accelDesp)*mf
print "Fuerza prom. despues: " + str(f1_despues) + ' N'

#Punto 9
#Como despues de tocar al piso la persona está somedida a la fuerza de su peso y de las piernas: F-W = m*a ---> F = W+ m*a   ( m*a es la fuerza promedio)
Fsuelo1 = mf*9.81 + f1_despues 
print "Fuerza ejercida por el suelo:"
print str(Fsuelo1) + 'N'

#punto 11 fuerza teórica del suelo:
#Corresponde a cuanta Energia tiene el cuerpo por unidad de distancia recorrida.

#Para Felipe
#Desde frame 95 (y = 1.058 m) hasta frame 98(y = 0.811 m)
print u"DATOS TEÓRICOS"
eSuelo1 = mf*9.81*0.98
print "Energia potencial en el piso al momento de impacto: " +  str(eSuelo1) + ' J'
FTeoSuelo1 = eSuelo1/abs(1.058 -0.811)
print str("Fuerza teorica del suelo: ") + str(FTeoSuelo1) + ' N'


print '\n'


#Para Andres (flexion amplia)
ma = 81 #kg
pa = 'C:\Users\juank\Desktop\Fisica\Taller2\datosAndres.txt'
datosAndres = separarDatos(pa)
acc2Antes = [] #los i <= 6
acc2Desp = [] #los i >6

for i in range(len(datosAndres)):
    if i <= 6:
        acc2Antes.append(datosAndres[i][1])
    else:
        acc2Desp.append(datosAndres[i][1])


#Punto 10
print "Datos de Andres - MUCHA FLEXION"
f2_antes = promedio(acc2Antes)*ma
print "Fuerza prom. antes: " + str(f2_antes) + ' N'

f2_despues = promedio(acc2Desp)*ma
print "Fuerza prom. desp: " + str(f2_despues) + ' N'

Fsuelo2 = ma*9.81 + f2_despues
print "Fuerza ejercida por el suelo:"
print str(Fsuelo2) + ' N'

#Para Andres:
#Desde frame 156 (y = 0.709 m) hasta frame 161(y = 0.372 m)
print u"DATOS TEÓRICOS"
eSuelo2 = ma*9.81*0.98
print "Energia potencial en el piso al momento de impacto: " +  str(eSuelo2) + ' J'
FTeoSuelo2 = eSuelo2/abs(0.709 -0.372)
print str("Fuerza teorica del suelo: ") + str(FTeoSuelo2) + ' N'




#############
#SECCION 3 - METODO DE EULER - graficas de posicion y velocidad en y

#Para Andres - 0.6 s, h = 0.033
h = 0.033
t = [i for i in np.arange(0.,0.6,h)]

ay0 = -9.81
ay = []
for i in range(len(t)):
    ay.append(ay0)

#Velocidad
vy = [0]
vy = metodoEuler(h,ay,vy)
#print vy

#posicion:
y = [0.98]
y = metodoEuler(h,vy,y)
"""
#Plot-----------------------------------------------------
fig = plt.figure(figsize=(20,16), dpi=50)
ax = fig.add_subplot(111)

ax.plot(t,y,linewidth=1,linestyle='-',marker='o',markersize=10,color='b')
#ax.plot(t,vy,marker='o',color='r')
ax.set_xlim(0,1)
ax.set_ylim(-0.8,1.2)
ax.set_xlabel('t(s)',fontsize=25)
ax.set_ylabel('y(m)',fontsize=25)
ax.tick_params(direction='out', length=6, width=2, labelsize=20)



#plt.savefig("sine.pdf")
#plt.draw()
plt.show()
"""

t = extraerDatos(datosFelipe,0)
print t



