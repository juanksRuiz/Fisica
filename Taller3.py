# -*- coding: utf8 -*-
def prodEscalar(u,v):
    if len(u) != len(v):
        return "ERROR: LOS VECOTRES NO TIENEN LA MISMA DIMENSION"
    s = 0
    for i in range(len(u)):
        s = s + u[i]*v[i]
    return s
def timesParticles(lp):
    #lp: lista de particulas
    dic = {}
    for i in lp:
        #print "-----------------------"
        #print "i: ",i.nombre
        times = []
        for j in lp:
            distintos = False
            if i != j:
                #print "DISTINTOS: ",DISTINTOS
                #print "Creando tiempo entre " +i.nombre + ' y ' +j.nombre
                distintos = True
                #print "distintos: ",distintos
                rij = []
                vij = []
                for k in range(len(i.posicion)):
                    rij.append(i.posicion[k] - j.posicion[k])
                    vij.append(i.velocidad[k] - j.velocidad[k])

                normRij = (prodEscalar(rij,rij))**(1./2.)
                normVij = (prodEscalar(vij,vij)**(1./2.))
                tij = (-prodEscalar(rij,vij) - ( (prodEscalar(rij,vij))**2 - (normVij**2)*((normRij**2) - (i.sigma**2)) )**1./2.)/normVij**2
                times.append([j.nombre,tij])
            #print 'confirmando distintos: ',distintos
                dic[i.nombre] = times
                
    return dic

def timesWall(lp,Lx,Ly):
    #lp: lista de particulas
    #Lx: amplitud en x de la caja
    #Ly: amplitud en y de la caja

    dic = {}
    times = []
    for i in lp:
        if i.velocidad[0] != 0:
            td = (Lx-(i.sigma /2.)- i.posicion[0])/i.velocidad[0]
            ti = ((i.sigma/2.) - i.posicion[0])/i.velocidad[0]
            if td > 0:
                times.append(['der',td])
            if ti > 0:
                times.append(['izq',ti])
        if i.velocidad[1] != 0:
            tar = (Ly-(i.sigma /2.)- i.posicion[1])/i.velocidad[1]
            tab = ((i.sigma/2.) - i.posicion[1])/i.velocidad[1]
            if tar >0:
                times.append(['arriba',tar])
            if tab >0:
                times.append(['abajo',tab])
        dic[i.nombre] = times
        times = []
    return dic

def times(lp,Lx,Ly):
    d = {}
    dPart = timesParticles(lp)
    dWall = timesWall(lp,Lx,Ly)

    if (len(dPart) == 0 and len(dWall) != 0):
        d = dWall
    elif len(dPart) != 0 and len(dWall) == 0:
        d = dPart
    else:
        for k in dPart.keys():
            for p in dWall.keys():
                if k == p:
                    d[k] = dPart[k] + dWall[k]
                
    return d
 
  
class Particle(object):
    def __init__(self,posicion,velocidad,diametro,idx):
        #posicion: lista de dos componentes: x y y
        #velocidad: lista de dos componentes: x y y
        #idx: indice para el nombre
        self.posicion = posicion
        self.velocidad = velocidad
        self.sigma = diametro
        self.nombre = 'p' + str(idx)

    def move(self,t):
      for i in range(len(self.posicion)):
        self.posicion[i] = self.posicion[i] + t*self.velocidad[i]
  
    

    
Lx = 10
Ly = 10

p1 = Particle([2,5],[2,0],0.5,1)
p2 = Particle([7,2],[0,0.5],0.5,2)
p3 = Particle([8,8],[-1,-1],0.5,3)
lp = [p1,p2,p3]

for p in lp:
    print p.nombre
    print p.posicion
    print p.velocidad
    print "------------------"
print times(lp,Lx,Ly)
##
##print "Posicion inicial de particula: ",p1.posicion
##p1.move(1)
##print "Posicion final de particula: ",p1.posicion
 

