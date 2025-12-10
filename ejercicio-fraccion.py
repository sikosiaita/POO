class Fraccion:
    def __init__(self, denominador, numerador):
        self.denominador = denominador
        self.numerador = numerador
        def __str__(self):
             return f"{self.numerador}/{self.denominador}"
        def __add__(self, other):
            num = self.numerador * other.denominador + other.numerador * self.denominador
            den = self.denominador * other.denominador
            return Fraccion(num, den)
        def __mul__(self, other):
            num = self.numerador * other.numerador
            den = self.denominador * other.denominador
            return Fraccion(num, den)
        def __eq__(self, other):
            return self.numerador * other.denominador == self.denominador * other.numerador
    
f1 = Fraccion(1, 2)
f2 = Fraccion(1, 2)
#suma = f1 + f2 #error 
multiplicacion = f1 * f2
igualdad1 = f1 == f2
igualdad2 = f1 == f2

print("Fraccion 1:", f1)
print("Fraccion 2:", f2)
#print(suma)
print(multiplicacion)
print(igualdad1)
print(igualdad2)