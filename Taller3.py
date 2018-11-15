class Particle(object):
    def __init__(self,poscicion,velocidad):
        #posicion: lista de dos componentes: x y y
        #velocidad: lista de dos componentes: x y y
        self.posicion = posicion
        self.velocidad = velocidad

    def move(self,h):
        for i in range(len(self.posicion)):
            self.posicion[i] = self.posicion[i] + h*self.velocidad(i)


def prodEscalar(u,v):
    if len(u) == len(v):
        return "ERROR: LOS VECOTRES NO TIENEN LA MISMA DIMENSION"
    s = 0
    for i in range(len(u)):
        s = s + u[i]*v[i]

    return s
    
def times(p1)
Lx = 10
Ly = 10
