class Personaje :
    def __init__(self,nombre:str,descripcion:str):
        self.nombre = nombre
        self.descripcion = descripcion
    

class PersonajeJugable(Personaje):
    def __init__(self,nombre:str,salud:int,rol:str,ataque:int,defensa:int,magia:int,descripcion:str,experiencia:int,nivel:int,habilidades:dict):
        super().__init__(nombre,descripcion)
        self.salud = salud
        self.rol = rol
        self.ataque = ataque
        self.defensa = defensa
        self.magia = magia
        self.experiencia = experiencia
        self.nivel = nivel
        self.habilidades = habilidades
    
class Enemigo(Personaje):
    def __init__(self, nombre:str,salud:int,ataque:int,defensa:int,nivel:int,habilidades:dict,descripcion:str):
        super().__init__(nombre, descripcion)
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
        self.nivel = nivel
        self.habilidades = habilidades