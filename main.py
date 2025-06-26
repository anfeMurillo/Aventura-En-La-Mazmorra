if __name__ == "__main__":

    print("Bienvenide a la Aventura en la Mazmorra")
    
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