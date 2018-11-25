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
def dist(u,v):
    if len(u)!= len(v):
        return 'ERROR EN LAS DIMENSIONES'
    dx = u[0] - v[0]
    dy = u[1] - v[1]
    return ((dx**2)+(dy**2))**1./2.

def Rij(pi,pj):
    rij = []
    for i in range(len(pi)):
        rij[i] = pi.posicion[i] - pj.posicion[i]

    return rij

def Vij(pi,pj):
    vij = []
    for i in range(len(pi)):
        vij[i] = pi.velocidad[i] - pj.velocidad[i]

    return vij

def changeMomentum(Lx,Ly,p1,p2):
    #p1: particula i
    #p2: particula j
    #asumiendo que hay colision:
    # Si choca con algún muro

    #Con el muro de la derecha
    if (p1.posicion[0] + p.sigma/2. >= Lx):
        p1.velocidad[0] = -p1.velocidad[0]
    if(p2.posicion[0] + p2.sigma/2. >= Lx):
        p2.velocidad[1] = - p2.velocidad[1]

    #Con el muro de la izquierda
    if (p1.posicion[0] - p.sigma/2. <= 0):
        p1.velocidad[0] = -p1.velocidad[0]
    if(p2.posicion[1] - p2.sigma/2. <= 0):
        p2.velocidad[1] = - p2.velocidad[1]

    #Con el muro de arriba
    if (p1.posicion[1] + p1.sigma/2. >= Ly):
        p1.velocidad[1] = -p1.velocidad[1]
    if(p2.posicion[1] + p2.sigma/2. >= Ly):
        p2.velocidad[1] = - p2.velocidad[1]

    #Con el muro de abajo
    if (p1.posicion[1] - p.sigma/2. <= 0):
        p1.velocidad[1] = -p1.velocidad[1]
    if(p2.posicion[1] - p2.sigma/2. <= 0):
        p2.velocidad[1] = - p2.velocidad[1]

    #Si hay choque entre las particulas
    if dist(p1.posicion,p2.posicion) == p1.sigma:
        rij = Rij(p1,p2)
        vij = Vij(p1,p2)
        #rij <--- rij/sigma
        for i in range(len(rij)):
            rij[i] = rij[i]/p1.sigma
    
        coef = prodEscalar(vij,rij)
        deltaV = []
        for i in range(len(rij)):
            deltaV[i] = -coef*rij[i]

        for i in range(len(p1.velocidad)):
            p1.velocidad[i] = p1.velocidad[i] + deltaV[i]
            p2.velocidad[i] = p2.velocidad[i] - deltaV[i]
            
        


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


def getParticle(i):
    for p in lp:
        if 'p'+str(i) == p.nombre:
            return p

print times(lp,Lx,Ly)
##
##print "Posicion inicial de particula: ",p1.posicion
##p1.move(1)
##print "Posicion final de particula: ",p1.posicion
 

