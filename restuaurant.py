class Pedido:
    def __init__(self, mesa):
        self.mesa = mesa
        self.platos = []
        self.total = 0.0
    def agregarplato(self, nombre, precio):
        self.platos.append((nombre, precio))
        self.calculartotal()
    def total(self):
        self.total = sum
