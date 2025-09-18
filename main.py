from clases.areas import Areas

def main():
    calculadora = Areas()

    while True:
        print("\nSeleccione una figura para calcular el área:")
        print("1. Rectángulo")
        print("2. Triángulo")
        print("3. Salir")

        opcion = input("Ingrese el número de la figura: ")

        if opcion == "1":
            calculadora.area_rectangulo()
        elif opcion == "2":
            calculadora.area_triangulo()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()