import time
import random
import personajes as p

enemigos_directorio = {
    1 : {
    "basicos" : {
        1 : p.Enemigo(
                nombre= "Troll",
                salud=60,
                ataque=6,
                nivel=1,
                imagen="🧌",
                descripcion="Es un Troll y ya"
        ),
        2 : p.Enemigo(
                nombre= "Calabera",
                salud=80,
                ataque=12,
                nivel=1,
                imagen="🩻",
                descripcion="Es una calabera esqueletica y ya"
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

diccionario = {}

def crear_combate (nivel:int,heroes:dict,tipo:str):
    
    n_enemigos = random.randint(1,3)
    
    for i in range(n_enemigos):
        i = i + 1
        r = random.randint(1,len(enemigos_directorio[nivel][tipo]))
        diccionario[i] = enemigos_directorio[nivel][tipo][r]
    
def enemigos_datos():
    for i in diccionario:
        diccionario[i].datos()
        
crear_combate(1,None,"basicos")
enemigos_datos()