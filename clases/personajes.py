class Personaje :
    def __init__(self,nombre:str,descripcion:str):
        self.nombre = nombre
        self.descripcion = descripcion
    

class PersonajeJugable(Personaje):
    
    def __init__(self,nombre:str,salud:int,rol:str,ataque:int,especial:int,magia:int,descripcion:str,experiencia:int,nivel:int):
        super().__init__(nombre,descripcion)
        self.salud = int(salud)
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
                    objetivo.salud = int(objetivo.salud)
            else:
                if len(objetivos) == 1 :
                    daño = self.ataque * valor_ataque
                    objetivos[0].salud -= (daño)
                    objetivos[0].salud = int(objetivos[0].salud)
                else:
                    print(
                        f"""
                        A cual enemigo atacar?
                        """)
                    for objetivo in objetivos:
                        i = 1
                        print(f"[{i}][{objetivo.nombre}]")
                        i += 1
                    respuesta = input(">>> ")
    
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
                            1 : {
                                "nombre" : "[corte rapido]",
                                "funcion": lambda objetivo : self.atacar(1,0,False,*objetivo)
                                },
                            2 : {
                                "nombre" : "[corte medio]",
                                "funcion": lambda objetivo : self.atacar(1.5,15,False,*objetivo)
                            },
                            3 : {
                                "nombre" : "[estocada final]",
                                "funcion": lambda objetivo : self.atacar(2,25,True,*objetivo)
                            }
                        },
                        "[habilidad]" : {
                            "[protegerse]" : None,
                            "[proteger a un compañero]" : None,
                            "[proteger a todo el grupo]" : None
                        }
                        },
                    (self.nivel == 2) : {
                        ...
                        },
                    (self.nivel == 3) : {
                        ...
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
                        "[habilidad]" : {
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
        
        print(
            f"""
            
            ____________________________________________________________
            
            {self.nombre}
            
            [{self.salud}][{(self.salud // 10) * "💖" }]
            
            [{self.magia}][{(self.magia // 10) * "🧿" }]
            
            ____________________________________________________________
            
            Opciones
            
            [⚔️][atacar]
            
            [💫][otro]
            
            """)
        
        def opciones_ataque():
            ataque_1 = lambda *args : self.habilidades[True]["[ataque]"][1]["funcion"](args)
            ataque_2 = lambda *args : self.habilidades[True]["[ataque]"][2]["funcion"](args)
            ataque_3 = lambda *args : self.habilidades[True]["[ataque]"][3]["funcion"](args)
            print(
                f"""
                [⚔️][atacar]
                
                [1][{self.habilidades[True]["[ataque]"][1]["nombre"]}]
                [2][{self.habilidades[True]["[ataque]"][2]["nombre"]}]
                [3][{self.habilidades[True]["[ataque]"][3]["nombre"]}]
                [4][volver atras]
                
                """)
            
            respuesta = input(">>> ")
            
            match respuesta:
                
                case "1" :
                    ataque_1(troll,troll_2)
                case "2" :
                    ataque_2(troll,troll_2)
                case "3" :
                    ataque_3(troll,troll_2)
                case "4" :
                    self.menu_batalla()
                
        def opciones_habilidad():
            ...
        
        pregunta = input(">>> ")
        
        if pregunta == "atacar":
            opciones_ataque()
        elif pregunta == "otro":
            ...
        else:
            #volver a preguntar
            ...
  
class Enemigo(Personaje):
    
    def __init__(self, nombre:str,salud:int,ataque:int,nivel:int,habilidades:dict,descripcion:str):
        super().__init__(nombre, descripcion)
        self.salud = salud
        self.ataque = ataque
        self.nivel = nivel
        self.habilidades = habilidades
        
    def datos(self):
        print(
            f"""
            {self.nombre}
            ____________________________________________________________
            
            [{self.salud}][{int(self.salud // 10) * "🖤" }]
            
            [👹][{self.nivel}]
            
            """)


troll = Enemigo(
    nombre= "Troll",
    salud=60,
    ataque=6,
    nivel=1,
    habilidades=None,
    descripcion="Es un Troll y ya"
)

troll_2 = Enemigo(
    nombre= "Troll",
    salud=60,
    ataque=6,
    nivel=1,
    habilidades=None,
    descripcion="Es un Troll y ya"
)

troll.datos()

troll_2.datos()

caballero = PersonajeJugable("Felipe",100,"caballero",10,5,100,None,0,1)

caballero.menu_batalla()

troll.datos()

troll_2.datos()