def sumar(num1, num2):
    return num1 + num2


def restar(numero1, numero2):
    return numero1 - numero2


def multiplicar(a, b):
    return a * b


def dividir(dividendo, divisor):
    if divisor == 0:
        print("no se puede dividir entre cero")
        return None
    return dividendo / divisor


if __name__ == "__main__":
    print("bienvenido a la calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    opcion = input("Elige una opcion: ")
    n1 = float(input("primer numero: "))
    n2 = float(input("segundo numero: "))
    if opcion == "1":
        print("El resultado es:", sumar(n1, n2))
    elif opcion == "2":
        print("El resultado es:", restar(n1, n2))
    elif opcion == "3":
        print("El resultado es:", multiplicar(n1, n2))
    elif opcion == "4":
        print("El resultado es:", dividir(n1, n2))
    else:
        print("opcion no valida")
