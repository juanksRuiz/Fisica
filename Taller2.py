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

#Salto POCA FLEXION
mf = 64.0 #kg
pf = 'C:\Users\juank\Desktop\Fisica\Taller2\PocaFlexion.txt'
datosFelipe = separarDatos(pf) #tiempo /v(m/s) / a(m/s^2)
accelAntes = [] #los i <= 6
accelDesp = [] #los i>6
for i in range(len(datosFelipe)):
    if i <= 6:
        accelAntes.append(datosFelipe[i][1])
    else:
        accelDesp.append(datosFelipe[i][1])

f1_antes = promedio(accelAntes)*mf
print "Datos  - POCA FLEXION"
print "Fuerza prom. antes: " + str(f1_antes) + ' N'

f1_despues = promedio(accelDesp)*mf
print "Fuerza prom. despues: " + str(f1_despues) + ' N'

#Punto 9
#Como despues de tocar al piso la persona está somedida a la fuerza de su peso y de las piernas: F-W = m*a ---> F = W+ m*a   ( m*a es la fuerza promedio)
Fsuelo1 = mf*9.8 + f1_despues 
print "Fuerza ejercida por el suelo:"
print str(Fsuelo1) + 'N'

#Fuerza teórica del suelo:
#Corresponde a cuanta Energia tiene el cuerpo por unidad de distancia recorrida.

#Desde frame 95 (y = 1.058 m) hasta frame 98(y = 0.811 m)
print u"DATOS TEÓRICOS"
#eSuelo1 = mf*9.81*0.98
vf = (2*9.8*0.98)**(1./2.)
eSuelo1 = (1./2.)*mf*vf**2
print "Energia potencial en el piso al momento de impacto: " +  str(eSuelo1) + ' J'
FTeoSuelo1 = eSuelo1/abs(1.058 -0.811)
print str("Fuerza teorica del suelo: ") + str(FTeoSuelo1) + ' N'


print '\n'


#SALTO - MUCHA FLEXION
p2 = 'C:\Users\juank\Desktop\Fisica\Taller2\MuchaFlexion.txt'
datosMF = separarDatos(p2)

acc2Antes = [] #los i <= 8
acc2Desp = [] #los i >8

for i in range(len(datosMF)):
    if i <= 8:
        acc2Antes.append(datosMF[i][1])
    else:
        acc2Desp.append(datosMF[i][1])




print "Datos - MUCHA FLEXION"
f2_antes = promedio(acc2Antes)*mf
print promedio(acc2Antes)
print "Fuerza prom. antes: " + str(f2_antes) + ' N'

f2_despues = promedio(acc2Desp)*mf
print "Fuerza prom. desp: " + str(f2_despues) + ' N'

Fsuelo2 = mf*9.8 + f2_despues
print "Fuerza ejercida por el suelo:"
print str(Fsuelo2) + ' N'


#Desde frame 101 (y = 0.960 m) hasta frame 110(y = 0.376 m)
print u"DATOS TEÓRICOS"
eSuelo2 = mf*9.8*0.98
print "Energia potencial en el piso al momento de impacto: " +  str(eSuelo2) + ' J'
FTeoSuelo2 = eSuelo2/abs(0.960 -0.376)
print str("Fuerza teorica del suelo: ") + str(FTeoSuelo2) + ' N'

#############
#SECCION 3 - METODO DE EULER - graficas de posicion y velocidad en y
#1) POCA FLEXION
#1.1) Caida libre

h = 0.1

t = [i for i in np.arange(0,0.8,h)]
g = 9.8
ay011 = -g
ay11 = [ay011]
for i in range(len(t)-1):
    ay11.append(ay011)

print t
#Velocidad
vy11 = [0]
vy11 = metodoEuler(h,ay11,vy11)
#print vy11

#posicion:
y11 = [0.98]
y11 = metodoEuler(h,vy11,y11)
#print "len(y11): ",len(y11)
#print "len(t): ",len(t)
print "----------------------"

#1.2) Despues de tocar el suelo
#Utilizando la fuerza teorica
ay012 = FTeoSuelo1 - g
ay12 = [ay012]

for i in range(len(t)-1):
    ay12.append(ay012)

#print ay12
#Velocidad
vf = (2*g*0.98)**(1.0/2.0)
vy12 = [-vf]
vy12 = metodoEuler(h,ay12,vy12)
#print vy12

#Posicion
y12 = [0.960]
y12 = metodoEuler(h,vy12,y12)


print '\n'
#2) MUCHA FLEXION
#2.1) Caida libre
ay021 = -g
ay21 = [ay021]
for i in range(len(t)-1):
    ay21.append(ay021)


#Velocidad
vy21 = [0]
vy21 = metodoEuler(h,ay21,vy21)
#print vy21

#posicion:
y21 = [0.98]
y21 = metodoEuler(h,vy11,y11)

#print "----------------------"

#2.2) Despues de tocar el suelo
#Utilizando la fuerza teorica
ay022 = FTeoSuelo2 - g
ay22 = [ay022]

for i in range(len(t)-1):
    ay22.append(ay022)

#print ay22
#Velocidad
vf = (2*g*0.98)**(1.0/2.0)
vy22 = [-vf]
vy22 = metodoEuler(h,ay22,vy22)
#print vy22

#Posicion
y22 = [0.960]
y22 = metodoEuler(h,vy22,y22)
#print y22
#print "len(y22): ",len(y22)
#print "len(t): ", len(t)
#print t
"""
#Plot-----------------------------------------------------
fig = plt.figure(figsize=(20,16), dpi=50)
ax = fig.add_subplot(111)
ax.plot(t,y11,linewidth=1,linestyle='-',marker='o',markersize=10,color='b')
#ax.plot(t,y22,marker='o',color='r')
ax.set_xlim(0,1)
ax.set_ylim(-0.8,1.2)
ax.set_xlabel('t(s)',fontsize=25)
ax.set_ylabel('y(m)',fontsize=25)
ax.tick_params(direction='out', length=6, width=2, labelsize=20)



#plt.savefig("sine.pdf")
#plt.draw()
plt.show()


#t = extraerDatos(datosFelipe,0)
#print t


"""
#################################
def lineaLatex(datos):
#Esribe la lista datos en una linea para tablero en formato Latex
    # en este caso, los distintos datos están ya en una lista
    if len(datos) == 0:
        print " ERROR: no hay datos en la lista ingresada"
        return
    else:
        output = '%s'
        if len(datos) > 1:
            for i in range(1,len(datos)):
                if i != (len(datos) -1):
                    output = output + '&%s'
                elif (i == (len(datos)-1)):
                    output = output + '&%s'+'\\' + '\\' + ' \\hline'
        else:
            output = output + '\\' + '\\'
        # Afuera de la función la persona elije los datos y su orden
        return output


def DatosALatex(listaDatos):
    #Dada una lista de listas de valores sacadas Tracker, escribe las listas en formato Latex
    #Primero Buscar las lineas necesarias en el txt, luego llamar a la funcion con esas lineas
    for entrada in listaDatos:
        s = entrada.replace(',','&')
        print (s + '\\' + '\\' + ' \\hline')

tiempo = [i for i in range(10)]
y = [i**2 for i in tiempo]
v = []
for i in range(len(tiempo)):
    v.append(5.3*i)

final =[tiempo,y,v]

for linea in datosFelipe:
    print lineaLatex(linea)
