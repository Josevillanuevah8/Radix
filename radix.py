
def radix_no_negativos(numeros):
    if len(numeros) == 0:
        return numeros

    mayor = max(numeros)
    posicion = 1

    while mayor // posicion > 0:
        cubetas = [[] for i in range(10)]

        for numero in numeros:
            digito = (numero // posicion) % 10
            cubetas[digito].append(numero)

        numeros = []

        for cubeta in cubetas:
            numeros.extend(cubeta)

        posicion *= 10

    return numeros


def radix_sort(numeros):
    negativos = []
    positivos = []

    for numero in numeros:
        if numero < 0:
            negativos.append(-numero)
        else:
            positivos.append(numero)

    negativos = radix_no_negativos(negativos)
    positivos = radix_no_negativos(positivos)

    negativos = [-n for n in reversed(negativos)]

    return negativos + positivos


while True:
    print("\n===== MENU RADIX SORT =====")
    print("1. Ordenar numeros")
    print("2. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        cantidad = int(input("Cuantos numeros desea ingresar: "))

        numeros = []
        for i in range(cantidad):
            numero = int(input(f"Ingrese el numero {i + 1}: "))
            numeros.append(numero)

        print("Numeros originales:", numeros)
        print("Numeros ordenados:", radix_sort(numeros))

    elif opcion == "2":
        print("Saliendo del programa...")
        break

    else:
        print("Opcion incorrecta, intente nuevamente.")
