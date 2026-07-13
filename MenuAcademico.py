# ==========================================
# Academia de Matemáticas
# Programa de operaciones recursivas
# ==========================================

# Constantes del menú no negocianbles
OPCION_POTENCIA = 1
OPCION_SUMA = 2
OPCION_FACTORIAL = 3
OPCION_REPORTE = 4
OPCION_SALIR = 5
OPCION_SUMA_DIGITOS = 6


def calcular_potencia(base, exponente):
    """
    Calcula la potencia de un número usando recursividad.

    Parámetros:
        base (int): número base.
        exponente (int): exponente.

    Regresa:
        int: resultado de base elevado al exponente.
    """
    if exponente == 0:
        return 1
    return base * calcular_potencia(base, exponente - 1)


def calcular_suma_acumulada(numero):
    """
    Calcula la suma desde 1 hasta un número usando recursividad.

    Parámetros:
        numero (int): número positivo.

    Regresa:
        int: suma acumulada.
    """
    if numero == 1:
        return 1
    return numero + calcular_suma_acumulada(numero - 1)


def calcular_factorial(numero):
    """
    Calcula el factorial usando recursividad.

    Parámetros:
        numero (int): número entero.

    Regresa:
        int: factorial del número.
    """
    if numero == 0:
        return 1
    return numero * calcular_factorial(numero - 1)


def calcular_suma_digitos(numero):
    """
    Calcula la suma de los dígitos usando recursividad.

    Parámetros:
        numero (int): número entero positivo.

    Regresa:
        int: suma de sus dígitos.
    """
    if numero < 10:
        return numero
    return numero % 10 + calcular_suma_digitos(numero // 10)


def mostrar_menu():
    """
    Muestra el menú principal.
    """
    print("\n========== Academia de Matemáticas ==========")
    print("1. Calcular potencia")
    print("2. Calcular suma acumulada")
    print("3. Calcular un factorial")
    print("4. Ver el reporte de la sesión")
    print("5. Salir")
    print("6. Calcular suma de dígitos")


def mostrar_reporte(historial):
    """
    Muestra el historial de operaciones realizadas.

    Parámetros:
        historial (list): lista con las operaciones.
    """
    print("\n========== REPORTE DE LA SESIÓN ==============")

    if len(historial) == 0:
        print("No hay operaciones registradas aún.")
        return

    print(f"{'No.':<5}{'Tipo':<20}{'Datos':<30}{'Resultado'}")

    potencias = 0
    sumas = 0
    factoriales = 0
    sumas_digitos = 0

    for operacion in historial:
        print(f"{operacion['operacion']:<5}{operacion['tipo']:<20}{operacion['datos']:<30}{operacion['resultado']}")

        if operacion["tipo"] == "Potencia":
            potencias += 1
        elif operacion["tipo"] == "Suma acumulada":
            sumas += 1
        elif operacion["tipo"] == "Factorial":
            factoriales += 1
        elif operacion["tipo"] == "Suma de dígitos":
            sumas_digitos += 1

    print("\nResumen")
    print("Potencias calculadas:", potencias)
    print("Sumas acumuladas calculadas:", sumas)
    print("Factoriales calculados:", factoriales)
    print("Sumas de dígitos calculadas:", sumas_digitos)
    print("Total de operaciones:", len(historial))


historial = []
numero_operacion = 1

while True:

    mostrar_menu()

    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Debe ingresar un número.")
        continue

    if opcion == OPCION_POTENCIA:

        base = int(input("Base: "))

        while True:
            exponente = int(input("Exponente: "))
            if exponente >= 0:
                break
            print("Error: el exponente no puede ser negativo.")

        resultado = calcular_potencia(base, exponente)

        print("Resultado:", resultado)

        historial.append({
            "operacion": numero_operacion,
            "tipo": "Potencia",
            "datos": f"Base={base}, Exp={exponente}",
            "resultado": resultado
        })

        numero_operacion += 1

    elif opcion == OPCION_SUMA:

        while True:
            numero = int(input("Número: "))
            if numero > 0:
                break
            print("Debe ser mayor que cero.")

        resultado = calcular_suma_acumulada(numero)

        print("Resultado:", resultado)

        historial.append({
            "operacion": numero_operacion,
            "tipo": "Suma acumulada",
            "datos": f"Número={numero}",
            "resultado": resultado
        })

        numero_operacion += 1

    elif opcion == OPCION_FACTORIAL:

        while True:
            numero = int(input("Número: "))
            if numero >= 0:
                break
            print("Debe ser mayor o igual a cero.")

        resultado = calcular_factorial(numero)

        print("Resultado:", resultado)

        historial.append({
            "operacion": numero_operacion,
            "tipo": "Factorial",
            "datos": f"Número={numero}",
            "resultado": resultado
        })

        numero_operacion += 1

    elif opcion == OPCION_REPORTE:
        mostrar_reporte(historial)

    elif opcion == OPCION_SALIR:
        print("Gracias por utilizar el sistema.")
        break

    elif opcion == OPCION_SUMA_DIGITOS:

        while True:
            numero = int(input("Número: "))
            if numero > 0:
                break
            print("Debe ser un número positivo.")

        resultado = calcular_suma_digitos(numero)

        print("Resultado:", resultado)

        historial.append({
            "operacion": numero_operacion,
            "tipo": "Suma de dígitos",
            "datos": f"Número={numero}",
            "resultado": resultado
        })

        numero_operacion += 1

    else:
        print("Opción inválida.")