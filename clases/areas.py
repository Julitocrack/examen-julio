
class Areas:
    def __init__(self):
        self.resultado = 0

    def area_rectangulo(self):
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        self.resultado = base * altura
        print(f"El área del rectángulo es: {self.resultado}")

    def area_triangulo(self):
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        self.resultado = (base * altura) / 2
        print(f"El área del triángulo es: {self.resultado}")
 