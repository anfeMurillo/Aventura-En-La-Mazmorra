class Personaje :
    def __init__(self,nombre:str,descripcion:str):
        self.nombre = nombre
        self.descripcion = descripcion
    

class PersonajeJugable(Personaje):
    
    def __init__(self,nombre:str,salud:int,rol:str,ataque:int,especial:int,magia:int,descripcion:str,experiencia:int,nivel:int):
        super().__init__(nombre,descripcion)
        self.salud = salud
        self.rol = rol
        self.ataque = ataque
        self.especial = especial
        self.magia = magia
        self.experiencia = experiencia
        self.nivel = nivel
        self.habilidades = {}
        self.definir_habilidades()

    def atacar(self,valor_ataque:int,costo_magia:int,grupal:bool,*objetivos:object):
        if self.magia >= costo_magia:
            if grupal == True:
                daño = self.ataque * valor_ataque
                self.magia -= costo_magia
                for objetivo in objetivos:
                    objetivo.salud -= (daño)
            else:
                daño = self.ataque * valor_ataque
                objetivos[0].salud -= (daño)
    
    def definir_habilidades(self):
        
        """
        Define las habilidades que un personaje puede usar o no.
        
        Esta funcion depende de la funcion atacar.
        
        >>> enemigo = Enemigo("Troll",100,None,None,None,None,None)

        >>> caballero = PersonajeJugable("Felipe",100,"caballero",5,5,100,None,0,1)

        >>> caballero.habilidades["nivel_1"]["[ataque]"]["[corte rapido]"](enemigo)
        
        >>> enemigo.salud
        95
        """
        
        match self.rol:
            
            case "caballero":
            
                self.habilidades = {
                    (self.nivel == 1) : {
                        "[ataque]" : {
                            "[corte rapido]" : lambda objetivo : self.atacar(1,0,False,objetivo),
                            "[corte medio]" : lambda objetivo : self.atacar(1.5,15,False,objetivo),
                            "[estocada final]" : lambda objetivo : self.atacar(2,25,False,objetivo)
                        },
                        "[defensa]" : {
                            "[propia]" : None,
                            "[a un compañero]" : None,
                            "[a todo el grupo]" : None
                        }
                        },
                    (self.nivel == 2) : {
                        "[ataque]" : {
                            "[corte rapido]" : lambda objetivo : self.atacar(2,0,False,objetivo),
                            "[corte medio]" : lambda objetivo : self.atacar(2.5,15,False,objetivo),
                            "[estocada final]" : lambda objetivo : self.atacar(3,25,False,objetivo)
                        },
                        "[defensa]" : {
                            "[propia]" : None,
                            "[a un compañero]" : None,
                            "[a todo el grupo]" : None
                        }
                        },
                    (self.nivel == 3) : {
                        "[ataque]" : {
                            "[corte rapido]" : lambda objetivo : self.atacar(3,0,False,objetivo),
                            "[corte medio]" : lambda objetivo : self.atacar(3.5,15,False,objetivo),
                            "[estocada final]" : lambda objetivo : self.atacar(4.5,25,False,objetivo)
                        },
                        "[defensa]" : {
                            "[propia]" : None,
                            "[a un compañero]" : None,
                            "[a todo el grupo]" : None
                        }
                    }
                }
                
            case "mago":

                self.habilidades = {
                    "nivel_1" : {
                        "[ataque]" : {
                            "[bola de fuego]" : None,
                            "[balas de piedra]" : None,
                            "[tormeta electrica]" : None
                        },
                        "[recuperacion]" : {
                            "[propia]" : None,
                            "[a un compañero]" : None,
                            "[a todo el grupo]" : None
                        }
                        },
                    "nivel_2" : {},
                    "nivel_3" : {}
                }
                
            case "ladron":

                self.habilidades = {
                    "nivel_1" : {
                        "[ataque]" : {
                            "[cuchilla voladora]" : ...,
                            "[bomba de humo]" : ...,
                            "[ataque de sombra]" : ...
                        },
                        "[habilidad]" : {
                            "[propia]" : ...,
                            "[a un compañero]" : ...,
                            "[a todo el grupo]" : ...
                        }
                        },
                    "nivel_2" : {},
                    "nivel_3" : {}
                }

    def menu_batalla (self):
        
        def opciones_ataque(enemigo = None):
            ataque_1 = lambda enemigo : self.habilidades[True]["[ataque]"]["[corte rapido]"](enemigo)
            ataque_1(enemigo)
        def opciones_habilidad():
            ...
        
        print(
            f"""
            {self.nombre} deberia?
            [⚔️][atacar]
            [💫][otro]
            """
            )
        pregunta = input(">>> ")
        
        if pregunta == "atacar":
            opciones_ataque(enemigo = troll)
        elif pregunta == "otro":
            ...
        else:
            #volver a preguntar
            ...
  
class Enemigo(Personaje):
    def __init__(self, nombre:str,salud:int,ataque:int,especial:int,nivel:int,habilidades:dict,descripcion:str):
        super().__init__(nombre, descripcion)
        self.salud = salud
        self.ataque = ataque
        self.especial = especial
        self.nivel = nivel
        self.habilidades = habilidades


troll = Enemigo("Troll",100,None,None,None,None,None)

caballero = PersonajeJugable("Felipe",100,"caballero",10,5,100,None,0,1)

caballero.menu_batalla()

print(troll.salud)