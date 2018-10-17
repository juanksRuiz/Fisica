#Metodo de euler
#Dada una lista de valores retorna una lista con los valores de la integral
 
import numpy as np
import matplotlib.pyplot as plt
 

 
 
#######################################
def metodoEuler(h,N,listaInput,listaIntegral):
     
    #Calculamos la integral
     
    for i in range(len(listaInput)-1):
        ival = listaIntegral[i] + h*listaInput[i]
        listaIntegral.append(ival)
         
    return listaIntegral

#pruebas
 
N = 1
h = 0.1
t = [i for i in np.arange(0.,N,h)]
ay =[]
for i in range(len(t)):
    ay.append(-9.8)

ax = []
for i in range(len(t)):
    ax.append(0)
    
    

 
#Velocidades
# Vy
vy0 = 5*np.sin(45) #5 es la magnitud de la velocidad 
vy = [vy0] 
vy = metodoEuler(h,N,ay,vy)

#print ay
#print "Cantidad de elementos en ay: " + str(len(ay))
#print vy
#print "Cantidad de elementos en vy: " + str(len(vy))


#Vx
vx0 = 5*np.cos(45)
vx = [vx0]
vx = metodoEuler(h,N,ax,vx)

#print ax
#print "Cantidad de elementos en ax: " + str(len(ax))
#print vx
#print "Cantidad de elementos en vx: " + str(len(vx))

#posiciones
#x(t)
x0 = 0
xt = [x0]
xt = metodoEuler(h, N, vx, xt)
print xt

y0 = 2
yt = [y0]
yt = metodoEuler(h, N, vy, yt)
print yt

#Graficas
t = [i for i in np.arange(0.,N,h)]

#Plot-----------------------------------------------------
fig = plt.figure(figsize=(20,16), dpi=50)
ax = fig.add_subplot(111)

ax.plot(xt,yt,linewidth=1,linestyle='-',marker='o',markersize=10,color='k')
ax.set_xlim(0,2.5)
ax.set_ylim(0,5)
ax.set_xlabel('x(m)',fontsize=25)
ax.set_ylabel('y(m)',fontsize=25)
ax.tick_params(direction='out', length=6, width=2, labelsize=20)

#plt.savefig("sine.pdf")
plt.draw()

plt.show()