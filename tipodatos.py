print("--Clases V2--Luis Orlando Sifuentes Montañez--")
print("--22308051281313--")
# zona de clase
class Datos:
    # el constructor
    def __init__ (self,estatura,peso):
        self.estatura = estatura
        self.peso = peso
    def mostrar_datos(self):
        print(f"Estatura: {self.estatura} mts, Peso {self.peso} Kg ")
    # LISTA
    def mi_lista(self):
        comidas=["Sushi", "Hamburguesas", "Pizza"]
        print(comidas)
        print("--COMiDAS CON LISTAS--")
        for x in comidas:
            print(x)
    # TUPLAS
    tuplarestaurantes = ("KFC", "WENDYS", "MCDONALS")
    print("--RESTAURANTES CON TUPLAS--")
    for x in tuplarestaurantes:
            print(x)
    # CONJUNTOS
    conjunto = {"RYZEN", "NVIDIA", "HP",}
    print("--COMPONENTES CON SETS--")
    for x in conjunto:
            print(x)
    # DICCIONARIO
    diccionario= {
        "PLAYSTATION": "5",
        "MODELO": "PRO",
        "AÑO": 2024
    }
    print("--PLAYSTATION CON DICCIONARIO--")
    for x, y in diccionario.items():
            print(x, y)
            
# creacion de objeto info
info=Datos(1.68,72.2)

# utilizando el obj. --> info
info.mostrar_datos()
info.mi_lista()
print("--Luis Orlando Sifuentes Montañez--")
