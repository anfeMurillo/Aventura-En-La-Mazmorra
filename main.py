if __name__ == "__main__":

    import pyfiglet as pft

    bienvenida = pft.figlet_format("Bienvenide a la Aventura en la Mazmorra",font="3-d")
    
    print(bienvenida)
    
    def inicio ():
        """Crea mensaje de inicio del juego"""
        print("Quieres empezar? [si] [no]")
        respuesta = input(">>> ")
        if respuesta == "si":
            ...
        elif respuesta == "no":
            print("Adios")
        else:
            print("Valor incorrecto, vuelve a intentarlo por favor")
            inicio()
    
    inicio()