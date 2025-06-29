import time

def dialogo(texto):
    """
    
    """
    lista = texto.split("\n")
    
    for frace in lista:
        time.sleep(0.5)
        print(frace)

heroes = []

if __name__ == "__main__":

    import pyfiglet as pft
    
    from clases import personajes as p
    
    import clases.combate as combate

    bienvenida = pft.figlet_format("Bienvenide a la Aventura en la Mazmorra",font="3-d")
    
    print(bienvenida)
    
    def inicio():
        
        """Crea mensaje de inicio del juego"""
        
        time.sleep(2)
        
        print(
            """
            🏰 Quieres empezar? 🧌 
            [si]
            [no]
            """
            )
        
        respuesta = input(">>> ")
        
        if respuesta == "si":
            ...
        elif respuesta == "no":
            
            print("Adios")
            
            exit()
        else:
            
            print("Valor incorrecto, vuelve a intentarlo por favor")
            
            inicio()
    
    inicio()
    
    introduccion = """
    🕯️ La Mazmorra de Ladagua 🕯️

    Se dice que en las profundidades del mundo existe una mazmorra viviente que nadie ha logrado conquistar.
    
    Sus muros susurran nombres olvidades, y cada paso es un descenso hacia lo desconocido.

    Construida por une antigüe hechicere que intentó encerrar el dolor del mundo, terminó atrapándose a sí misme.
    
    Ahora, besties, trampas y acertijos habitan en sus pasillos cambiantes.

    Poc@s han entrado. Ningune ha salido.

    Y sin embargo, ahí estás. No sabés quién sos ni por qué viniste, pero sentís el llamado.

    ¿Buscás gloria? ¿Redención? ¿O simplemente un lugar donde pertenecer?
    
    Ladagua te ha elegido. 
    
    La mazmorra respira.
    
    Tu historia comienza ahora.
    """
        
    dialogo(introduccion)
    
    time.sleep(2)
    
    print(
        """
        🤔 Cual es tu nombre de leyenda ?
        """
        )
    
    jugador_name = input(">>> ")
    
    time.sleep(2)
    
    print(
        """
        Cual es tu rol?
        
        ⚔️ [caballero]
        
        🧙 [mago]
        
        🥷 [ladron]
        """)
    
    jugador_rol = input(">>> ")
    
    time.sleep(2)
    
    print(
        """
        Se va a crear tu personaje 😃
        """
        )
    
    heroe_principal = p.PersonajeJugable(jugador_name,100,jugador_rol,10,10,50,"una leyenda que aparecio en este lugar.")
    
    heroes.append(heroe_principal)
    
    combate.crear_combate(nivel=1,heroes=heroes,tipo="basicos")