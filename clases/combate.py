import time
import random
from . import personajes as p

enemigos_directorio = {
    1 : {
    "basicos" : {
        1 : p.Enemigo(
                nombre= "Troll",
                salud=60,
                ataque=10,
                nivel=1,
                imagen="🧌",
                descripcion="Es un Troll y ya",
        ),
        2 : p.Enemigo(
                nombre= "Calabera",
                salud=80,
                ataque=12,
                nivel=1,
                imagen="🩻",
                descripcion="Es una calabera esqueletica y ya",
        ),
        3 : p.Enemigo(
                nombre= "Demonio",
                salud=75,
                ataque=20,
                nivel=1,
                imagen="👹",
                descripcion="Demonio herrante por el mundo",
        )
        },
    "sub-jefes" : ...,
    "jefes" : ...
    },
    2 : {
    "basicos" : ...,
    "sub-jefes" : ...,
    "jefes" : ...
    },
    3 : {
    "basicos" : ...,
    "sub-jefes" : ...,
    "jefes" : ...
    }
}

enemigos_turno = {}

def crear_combate (nivel:int,heroes:dict,tipo:str):
    
    n_enemigos = random.randint(1,3)
    
    for i in range(n_enemigos):
        i = i + 1
        r = random.randint(1,len(enemigos_directorio[nivel][tipo]))
        enemigos_turno[str(i)] = enemigos_directorio[nivel][tipo][r]
        
    
    def aliados_vivos():
        
        lista = []
        
        for heroe in heroes:
            
            lista.append(heroe.vivo)
            
        if True in lista:
            
            return True
        
        else:
            
            return False
    
    def enemigos_vivos():
        
        lista = []
        
        for enemigo in enemigos_turno:
            
            lista.append(enemigos_turno[enemigo].vivo)
            
        if True in lista:
            
            return True
        
        else:
            
            return False
        
    while ((aliados_vivos() and enemigos_vivos())):
        
        enemigos_datos()
        
        for heroe in heroes:
            
            heroe.menu_batalla()
    
def enemigos_datos():
    for i in enemigos_turno:
        enemigos_turno[i].datos()