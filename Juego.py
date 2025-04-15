class Juego:
    def __init__(self, nombre_jugador):
      
        self.nombre_jugador = nombre_jugador
        self.jugando = False
        self.contador = 0
    def iniciar_juego(self):
        self.jugando = True
        print(f"\n¡Bienvenido al juego, {self.nombre_jugador}!")
        print("El juego ha comenzado..")
        
        mensaje=input("Introducir mensaje: ").upper()
        P_Cod=0
        print("¡Gracias por jugar!\n")
        
        Codificado=self.codificar(mensaje)
        descodificado=self.descodificar(mensaje)
        print(f"El mensaje codificado es {Codificado} "
              "Y las palabras codificadas son",self.contador)
        print(f"El mensaje descodificado es {descodificado}")

            
    def salir(self):
        print(f"\nHasta luego, {self.nombre_jugador}. ¡Vuelve pronto!")

            
    def codificar(self,mensaje):
        self.contador +=1
        Codificado=""
        Abecedario= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        for letra in mensaje:
            num=Abecedario.index(letra)
            Espacio_L=num+1
            Codificado+=Abecedario[Espacio_L]
        print(f"contador {self.contador}")
        return Codificado
    
    
    def descodificar(self,mensaje):
        descodificado=""
        self.contador +=1
        Abecedarioa= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        for letras in mensaje:
                num=Abecedarioa.index(letras)
                Espacio_L=num-1
                descodificado+=Abecedarioa[Espacio_L]
        return descodificado
    
            
            
        


  
    


