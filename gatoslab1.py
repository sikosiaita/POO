class Gato:
    def __init__(self, nombre, edad, energia, hambre):
        self.nombre = nombre
        self.edad = edad
        self.energia = energia
        self.hambre = hambre
    
    def juego(self):
        if self.energia >= 10:
            self.energia -=10
            self.hambre += 15
            print(f"{self.nombre}, jugó y ahora tiene {self.energia} de energía y {self.hambre} de hambre.")
        else:
            print(f"{self.nombre} no tiene energia y no puede jugar.")
    def hambre(self):
        self.hambre -=20
        if self.hambre < 0:
            self.hambre = 0
        self.energia +=10
        if self.energia > 100:
            self.energia = 100
            print(f"{self.nombre} comió y ahora tiene {self.energia} de energía y {self.hambre} de hambre.")
    def __str__(self):
        return(f"Gato: {self.nombre}\n"
               f"Edad: {self.edad} años\n"
               f"Energia: {self.energia}/100\n"
               f"Hambre: {self.hambre}/100")
    def __del__(self):
        print(f"El gatito {self.nombre}, ha salido del café.")

gato1 = Gato("Michi", 3, 50, 30)
print(gato1) 

class EspacioCafe:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.gatopresente = []
    def agregargato(self, gato):
        if len(self.gatopresente) < self.capacidad:
            print(f"Gatito/a {gato.nombre}, ahora está en {self.nombre}")
        else:
            print(f"No hay espacio en {self.nombre} para {gato.nombre}")
    def mostrargatos(self):
        if self.gatopresente:
            print(f"Gatos presentes en {self.nombre}")
            for gato in self.gatopresente:
                print(f"-{gato.nombre}")

gato1 = Gato("Michi", 3, 50, 30)
gato2 = Gato("July", 4, 50, 30)
terraza = EspacioCafe("Terraza", 2)
terraza.agregargato(gato1)
terraza.agregargato(gato2)

terraza.mostrargatos()
