class Coche:
    def __init__(self, marca: str, gasolina: float):
        self.marca = marca
        self.gasolina = gasolina
        self.kilometrosrec = 0
    def conducir(self, km: float):
        litros_necesarios = km / 10
        if self.gasolina >= litros_necesarios:
            self.kilometrosrec += km 
            self.gasolina -= litros_necesarios
            print(f"El coche {self.marca} recorrió {km} kilometros, gasolina restante: {self.gasolina}")
        else:
            km_posibles = self.gasolina * 10
            self.kilometrosrec += km_posibles
            self.gasolina = 0
            print(f"El coche {self.marca} se ha quedado sin gasolina, recorrió {km_posibles}")
    def cargar_gasolina(self, litros: float):
        self.gasolina += litros
        print("Se cargaron {litros} de gasolina, ahora hay {self.gasolina} litros.")

micoche = Coche("Toyota", 5)
micoche.conducir(30)