import time

def dialogo(texto):
    """
    
    """
    lista = texto.split("/n")
    
    for frace in lista:
        time.sleep(1.5)
        print(frace)

if __name__ == "__main__":

    import pyfiglet as pft

    bienvenida = pft.figlet_format("Bienvenide a la Aventura en la Mazmorra",font="3-d")
    
    print(bienvenida)
    
    def inicio():
        
        """Crea mensaje de inicio del juego"""
        
        time.sleep(2)
        
        print("Quieres empezar? [si] [no]")
        
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
        /n
        Dicen que en lo más profundo del mundo, donde la piedra respira y la oscuridad piensa, existe una mazmorra 
        que nadie ha logrado conquistar. Sus muros murmuran nombres olvidades, y cada escalón hacia abajo es un 
        paso hacia lo desconocido.
        /n
        Esta no es una prisión cualquiera. Es un ser viviente. Un laberinto que cambia, que se alimenta del miedo 
        de quienes se atreven a entrar. Se dice que fue construida por une antigüe hechicere que quiso encerrar 
        el dolor del mundo… pero terminó encerrándose a sí misme.
        /n
        Besties deformes, acertijos imposibles, trampas silenciosas y pasillos sin fin esperan a quien se atreva 
        a cruzar sus puertas. Pocas personas han entrado. Ningune ha salido.
        /n
        Y sin embargo, aquí estás. Frente a la entrada, con el corazón latiendo como un tambor de guerra. 
        No sabés quién sos realmente, ni por qué estás acá… pero algo te llama desde el fondo.
        /n
        ¿Entrás para buscar gloria? ¿Redención? ¿O simplemente porque ya no hay otro lugar adonde ir?
        /n
        Ladagua te ha elegido. La mazmorra respira. Y tu historia… acaba de comenzar."""
        
    dialogo(introduccion)