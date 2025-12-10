class Cafe:
    def __init__(self, salon, terraza, zonajuego, gatito):
        self.salon = salon
        self.terraza = terraza
        self.zonajuego = zonajuego
        self.gatito = gatito
    def salon(self):
        if self.salon <= 5:
            self.gatito += 5
            