class Juego:
    def __init__(self, nombre_jugador):
      
        self.nombre_jugador = nombre_jugador
        self.jugando = False

    def iniciar_juego(self):
        self.jugando = True
        print(f"\n¡Bienvenido al juego, {self.nombre_jugador}!")
        print("El juego ha comenzado..")
        
        key= input()
        mensaje=input("Introducir mensaje: ").upper()
        
        print("¡Gracias por jugar!\n")
        
        Codificado=self.codificar(mensaje)
        descodificado=self.descodificar(mensaje)
        print(f"El mensaje codificado es {Codificado} ")
        print(f"El mensaje descodificado es {descodificado} ")

            
    def salir(self):
        print(f"\nHasta luego, {self.nombre_jugador}. ¡Vuelve pronto!")

            
    def codificar(self,mensaje):
        Codificado=""
        Abecedario= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        for letra in mensaje:
            num=Abecedario.index(letra)
            Espacio_L=num+1
            Codificado+=Abecedario[Espacio_L]
        return Codificado
    
    
    def descodificar(self,mensaje):
        descodificado=""
        Abecedarioa= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        for letras in mensaje:
                num=Abecedarioa.index(letras)
                Espacio_L=num-1
                descodificado+=Abecedarioa[Espacio_L]
        return descodificado
    
            
            
        


  
    


