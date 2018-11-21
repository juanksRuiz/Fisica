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
        times = []
        for j in lp:
            rij = []
            vij = []
            for k in range(len(i.posicion)):
                rij.append(i.posicion[k] - j.posicion[k])
                vij.append(i.velocidad[k] - j.velocidad[k])
            normRij = (prodEscalar(rij,rij))**(1./2.)
            normVij = (prodEscalar(vij,vij)**(1./2.))
            tij = (-prodEscalar(rij,vij) - ( (prodEscalar(rij,vij))**2 - (normVij**2)*((normRij**2) - (i.sigma**2)) )**1./2.)/normVij**2
            times.append(tij)
        dic[i] = times

    return dic

def timesWall(lp,Lx,Ly):
    #lp: lista de particulas
    #Lx: amplitud en x de la caja
    #Ly: amplitud en y de la caja

    dic = {}
    times = []
    for i in lp:
        td = (Lx-(i.sigma /2.)- i.posicion[0])/i.velocidad[0]
        ti = ((i.sigma/2.) - i.posicion[0])/i.velocidad[0]
        tar = (Ly-(i.sigma /2.)- i.posicion[1])/i.velocidad[1]
        tab = ((i.sigma/2.) - i.posicion[1])/i.velocidad[1]
        times.append(td)
        times.append(ti)
        times.append(tar)
        times.append(tab)
        dic[i] = times
        times = []
    return dic

def  times
        
        
              
        
          
          
 
  
class Particle(object):
    def __init__(self,posicion,velocidad,diametro):
        #posicion: lista de dos componentes: x y y
        #velocidad: lista de dos componentes: x y y
        self.posicion = posicion
        self.velocidad = velocidad
        self.sigma = diametro

    def move(self,t):
      for i in range(len(self.posicion)):
        self.posicion[i] = self.posicion[i] + t*self.velocidad(i)
  
    

    
Lx = 10
Ly = 10
