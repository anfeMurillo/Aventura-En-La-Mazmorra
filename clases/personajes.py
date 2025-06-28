import time as t

from main import heroes

class Personaje :
    def __init__(self,nombre:str,descripcion:str):
        self.nombre = nombre
        self.descripcion = descripcion
        self.vivo = True
    

class PersonajeJugable(Personaje):
    
    def __init__(self,nombre:str,salud:int,rol:str,ataque:int,especial:int,magia:int,descripcion:str):
        super().__init__(nombre,descripcion)
        self.salud = int(salud)
        self.rol = rol
        self.ataque = ataque
        self.especial = especial
        self.magia = magia
        self.experiencia = 0
        self.nivel = 1
        self.habilidades = {}
        self.definir_habilidades()
        
        if self.salud <= 0:
            self.vivo = False
            print(f"☠️ El personaje {self.nombre} esta muerto ☠️")

    def atacar(self,valor_ataque:int,costo_magia:int,grupal:bool,**objetivos:object):
        if self.magia >= costo_magia:
            if grupal:
                daño = self.ataque * valor_ataque
                self.magia -= costo_magia
                for objetivo in objetivos:
                    objetivos[objetivo].salud -= daño
                    objetivos[objetivo].salud = int(objetivos[objetivo].salud)
            else:
                if len(objetivos) == 1 :
                    daño = self.ataque * valor_ataque
                    objetivos[str(1)].salud -= daño
                    objetivos[str(1)].salud = int(objetivos[str(1)].salud)
                else:
                    print(
                        f"""
                        A cual enemigo atacar?
                        """)
                    i = 1
                    for objetivo in objetivos:
                        print(f"[{(i)}][{objetivos[objetivo].nombre}]")
                        i += 1
                        
                    respuesta = int(input(">>> "))
                    daño = self.ataque * valor_ataque
                    objetivos[str(respuesta)].salud -= daño
                    objetivos[str(respuesta)].salud = int(objetivos[str(respuesta)].salud)
        else:
            print("\n No tienes suficiente magia para esto.")
            t.sleep(2)
            self.menu_batalla()

    def proteger(self,valor_proteccion:int,costo_magia:int,grupal:bool,*aliados:object):
        
        if self.magia >= costo_magia:
            
            if grupal:
                
                if len(aliados) > 1:
                        
                    for aliado in aliados:
                        aliado.salud += valor_proteccion
                    
                    t.sleep(1.5)
                    
                    print(
                        f"""
                        🛡️ El aliado {aliado.nombre} ha recibido +{valor_proteccion} de proteccion 🛡️
                        """)
                    
                    t.sleep(1.5)
                
                else:
                    
                    print(
                        f"""
                        A cual aliado proteger?
                        """)
                    i = 1
                    for aliado in aliados:
                        print(f"[{(i)}][{aliado.nombre}]")
                        i += 1
                    
                    respuesta = int(input(">>> "))
                    
                    aliados[respuesta-1].salud += valor_proteccion
                    
                    t.sleep(1.5)
                    
                    print(
                        f"""
                        
                        🛡️ {aliados[respuesta-1].nombre} ha recibido + {valor_proteccion} de proteccion 🛡️
                        
                        """)
                    
                    t.sleep(1.5)
                
            else:
                self.salud += valor_proteccion
                
                t.sleep(1.5)
                
                print(
                    f"""
                    🛡️ {self.nombre} ha recibido + {valor_proteccion} de proteccion 🛡️
                     """)
                
                t.sleep(1.5)
        else:
            print("\n No tienes suficiente magia para esto.")
            t.sleep(2)
            self.menu_batalla()
    
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
                                "funcion": lambda **args : self.atacar(1,0,False,**args)
                                },
                            2 : {
                                "nombre" : "[corte medio]",
                                "funcion": lambda **args : self.atacar(1.5,15,False,**args)
                            },
                            3 : {
                                "nombre" : "[estocada final]",
                                "funcion": lambda **args : self.atacar(2,25,True,**args)
                            }
                        },
                        "[habilidad]" : {
                            1 : {
                                "nombre" : "[protegerse]",
                                "funcion": lambda arg : self.proteger(15,5,False)
                                },
                            2 : {
                                "nombre" : "[proteger a un compañero]",
                                "funcion": lambda arg : self.proteger(15,10,True,*arg)
                            },
                            3 : {
                                "nombre" : "[proteger a todo el grupo]",
                                "funcion": lambda arg : self.proteger(10,15,True,*arg)
                            }
                        }
                        },
                    (self.nivel == 2) : {
                        "[ataque]" : {
                            1 : {
                                "nombre" : "[corte rapido II]",
                                "funcion": lambda args : self.atacar(1,0,False,*args)
                                },
                            2 : {
                                "nombre" : "[corte medio II]",
                                "funcion": lambda args : self.atacar(1.5,15,False,*args)
                            },
                            3 : {
                                "nombre" : "[estocada final II]",
                                "funcion": lambda args : self.atacar(2,25,True,*args)
                            }
                        },
                        "[habilidad]" : {
                            1 : {
                                "nombre" : "[protegerse II]",
                                "funcion": lambda arg : self.proteger(25,5,False)
                                },
                            2 : {
                                "nombre" : "[proteger a un compañero II]",
                                "funcion": lambda arg : self.proteger(35,10,True,arg)
                            },
                            3 : {
                                "nombre" : "[proteger a todo el grupo II]",
                                "funcion": lambda arg : self.proteger(20,15,True,*arg)
                            }
                        }
                        },
                    (self.nivel == 3) : {
                        "[ataque]" : {
                            1 : {
                                "nombre" : "[corte sombrio]",
                                "funcion": lambda args : self.atacar(1,0,False,*args)
                                },
                            2 : {
                                "nombre" : "[espiral de acero]",
                                "funcion": lambda args : self.atacar(1.5,15,False,*args)
                            },
                            3 : {
                                "nombre" : "[estocada final III]",
                                "funcion": lambda args : self.atacar(2,25,True,*args)
                            }
                        },
                        "[habilidad]" : {
                            1 : {
                                "nombre" : "[protegerse III]",
                                "funcion": lambda arg : self.proteger(25,5,False)
                                },
                            2 : {
                                "nombre" : "[proteger a un compañero III]",
                                "funcion": lambda arg : self.proteger(40,10,True,arg)
                            },
                            3 : {
                                "nombre" : "[proteger a todo el grupo III]",
                                "funcion": lambda arg : self.proteger(30,15,True,*arg)
                            }
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
        
        def opciones_ataque():
            from .combate import enemigos_turno
            ataque_1 = lambda **args : self.habilidades[True]["[ataque]"][1]["funcion"](**args)
            ataque_2 = lambda **args : self.habilidades[True]["[ataque]"][2]["funcion"](**args)
            ataque_3 = lambda **args : self.habilidades[True]["[ataque]"][3]["funcion"](**args)
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
                    ataque_1(**enemigos_turno)
                case "2" :
                    ataque_2(**enemigos_turno)
                case "3" :
                    ataque_3(**enemigos_turno)
                case "4" :
                    self.menu_batalla()
                
        def opciones_habilidad():
            
            habilidad_1 = lambda *args : self.habilidades[True]["[habilidad]"][1]["funcion"](args)
            habilidad_2 = lambda *args : self.habilidades[True]["[habilidad]"][2]["funcion"](args)
            habilidad_3 = lambda *args : self.habilidades[True]["[habilidad]"][3]["funcion"](args)
            print(
                f"""
                [💫][habilidad]
                
                [1][{self.habilidades[True]["[habilidad]"][1]["nombre"]}]
                [2][{self.habilidades[True]["[habilidad]"][2]["nombre"]}]
                [3][{self.habilidades[True]["[habilidad]"][3]["nombre"]}]
                [4][volver atras]
                
                """)
            
            respuesta = input(">>> ")
            
            match respuesta:
                
                case "1" :
                    habilidad_1(heroes)
                case "2" :
                    habilidad_2(heroes)
                case "3" :
                    habilidad_3(heroes)
                case "4" :
                    self.menu_batalla()
        
        if self.vivo:
        
            print(
                f"""
                
                ____________________________________________________________
                
                {self.nombre}
                
                [{self.salud}][{(self.salud // 10) * "💖" }]
                
                [{self.magia}][{(self.magia // 10) * "🧿" }]
                
                ____________________________________________________________
                
                Opciones
                
                [⚔️][1][atacar]
                
                [💫][2][habilidad]
                
                """)
            
            pregunta = input(">>> ")
            
            if pregunta == "1":
                t.sleep(2)
                opciones_ataque()
            elif pregunta == "2":
                t.sleep(2)
                opciones_habilidad()
            else:
                #volver a preguntar
                
                t.sleep(2)
                
                print("\n ⚠️ Valor no permitido, vuelve a intentar")
                
                t.sleep(2)
                
                self.menu_batalla()
  
class Enemigo(Personaje):
    
    def __init__(self, nombre:str,salud:int,ataque:int,nivel:int,imagen:str,descripcion:str):
        super().__init__(nombre, descripcion)
        self.salud = salud
        self.ataque = ataque
        self.nivel = nivel
        self.imagen = imagen
        
        if self.salud <= 0:
            self.vivo = False
            print(f"☠️ El enemigo {self.nombre} esta muerto ☠️")
        
    def datos(self):
        if self.vivo:
            t.sleep(1)
            
            print(
                f"""
                {self.nombre}
                ____________________________________________________________
                
                [{self.salud}][{int(self.salud // 10) * "🖤" }]
                
                [{self.imagen}][{self.nivel}]
                
                """)