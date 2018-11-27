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

def changeMomentum(Lx,Ly,pi,pj):
    #Cambia el momento dado que ya hay colision entre dos paritculas o entre particula y muro
    if dist(pi,pj) == (pi.sigma)/2.:
	rij = Rij(pi,pj)
	vij = Vij(pi,pj)
	rsigma = rij
	for i in range(len(rsigma)):
	    rsigma[i] = float(rsigma[i]/pi.sigma)
	c = prodEscalar(vij,rsigma)
	vPara = rsigma
	for i in range(len(vPara)):
	    vPara[i] = c*vPara[i]

	deltaV = []
	for i in range(len(vPara)):
	    deltaV[i] = -vPara[i]
	    pi.velocidad[i] = pi.velocidad[i] + deltaV[i]
	    pj.velocidad[i] = pj.velocidad[i] - deltaV[i]
    else:
	if((pi.posicion[0] + pi.sigma/2. == Lx) or (pi.posicion[0] - pi.sigma/2. == 0)):
	    pi.velocidad[0] = pi.velocidad[0]
	if((pj.posicion[0] + pj.sigma/2. == Lx) or (pj.posicion[0] - pj.sigma/2. == 0)):
	    pj.velocidad[0] = pj.velocidad[0]

	if((pi.posicion[1] + pi.sigma/2. == Ly) or (pi.posicion[1] - pi.sigma/2. == 0)):
	    pi.velocidad[1] = pi.velocidad[1]
	if((pj.posicion[1] + pj.sigma/2. == Ly) or (pj.posicion[1] - pj.sigma/2. == 0)):
	    pj.velocidad[1] = pj.velocidad[1]

	
	
	

            
            

def avanzarSistema(n,lp,Lx,Ly):
    #pathCasa = 'C:\Users\juank\Desktop\Fisica\DatosTaller3.txt'
    #file = open(pathCasa,'w')

    pathUniv = '/home/vonnewmann/Escritorio/Fisica/DatosTaller3.txt'
    file = open(pathUniv,'w')
    h = ''
    pi = ''
    for p in lp:
        h = h+ '&'+str(p.nombre)
        pi = pi+'&'+str(p.posicion)
        T = 0.0
    file.write('Tiempo(s)' + h + '\\' + '\\' + '\n')
    regIni = str(T)+pi + '\\' + '\\' + '\n'
    file.write(regIni)
    
    #buscando minimo
    tmin = times(lp,Lx,Ly)['p1'][0][1]

    #print tmin
    colisiones = times(lp,Lx,Ly)
    
    for k in colisiones.keys():
	if colisiones[k] < tmin:
		tmin = colisiones[k]
	
    #Moviendo el sistema:
    for p in lp:
	p.move(tmin)
    
    
    file.close()




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
            self.posicion[i] = self.velocidad[i]*t + self.posicion[i]
        
        
    

    
Lx = 10
Ly = 10

p1 = Particle([2,2],[5,0],1,1)

p2 = Particle([4,2],[-1,0],1,2)
#p3 = Particle([8,8],[-1,-1],0.5,3)
lp1 = [p1]
lp2 = [p1,p2]
print times(lp1,Lx,Ly)
"""
print p1.nombre
print"posicion de p1"
print p1.posicion
p1.move(3)
print"posicion de p1"
print p1.posicion
"""
#avanzarSistema(3,lp,Lx,Ly)


#avanzarSistema(5,lp,Lx,Ly)

def getParticle(i):
    #Retorna la particula con el indice
    for p in lp:
        if 'p'+str(i) == p.nombre:
            return p


