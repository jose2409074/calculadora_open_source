import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

def mostrar_menu():
    """
    Muestra el menú de opciones de la calculadora.
    """
    print("\n--- Calculadora de Código Abierto ---")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Suma de N números")
    print("6. Salir")
    print("-----------------------------------")

def main():
    """
    Función principal que ejecuta la calculadora.
    """
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-6): ")

        if opcion == '6':
            print("¡Gracias por usar esta calculadora open source!")
            break

        if opcion in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingresa números.")
                continue

            if opcion == '1':
                resultado = sumar.sumar(num1, num2)
                print(f"El resultado de la suma es: {resultado}")
            elif opcion == '2':
                resultado = resta.restar(num1, num2)
                print(f"El resultado de la resta es: {resultado}")
            elif opcion == '3':
                resultado = multiplicacion.multiplicar(num1, num2)
                print(f"El resultado de la multiplicación es: {resultado}")
            elif opcion == '4':
                resultado = dividir.dividir(num1, num2)
                print(f"El resultado de la división es: {resultado}")

        elif opcion == '5':
            try:
                numeros_input = input("Ingresa los números a sumar, separados por espacios: ")
                numeros = [float(num) for num in numeros_input.split()]
                resultado = suma_avanzada.suma_avanzada(*numeros)
                print(f"El resultado de la suma avanzada es: {resultado}")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa solo números.")

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()