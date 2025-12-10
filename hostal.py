class Hostal:
    def __init__(self, cliente, entrada, salida, habitacion):
        self.cliente = cliente
        self.entrada = entrada
        self.salida = salida
        self.habitacion = habitacion

    def estadia(self):
            diaentrada, mesentrada, anioentrada = map(int, self.entrada.split('-'))
            diasalida, messalida, aniosalida = map(int, self.salida.split('-'))
            return diasalida - diaentrada

    def __str__(self):
             return (f"Reserva de {self.cliente}\n"
                f"Habitación: {self.habitacion}\n"
                f"Fecha de entrada: {self.entrada}\n"
                f"Fecha de salida: {self.salida}\n"
                f"Duración: {self.estadia()} días")
        
    def cambiarfecha(self, nuevasalida):
            self.salida = nuevasalida
            return f"Su nueva fecha de salida es: {self.salida}"
        
    def __del__(self):
            print(f"La reserva de {self.cliente} ha sido cancelada.")
reserva1= Hostal("Pia", "01-10-25", "02-10-25", "102")
print(reserva1)