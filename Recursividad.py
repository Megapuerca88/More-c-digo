# La recursividad es cuando una función se llama a sí misma 
#para resolver un problema, dividiéndolo en una versión más
# pequeña del mismo problema, hasta llegar a un punto
#tan simple que ya no necesita dividirse más.

def contar_sinlimite(numero):
    print(numero)
    contar_sinlimite(numero + 1)#Se llama a si mismo siempre
    #No hay nada que detenga esto

#contar_sinlimite(1)

def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n+1):
        resultado = resultado * i
    return resultado

print(f"Factorial iterativo de 5: {factorial_iterativo(5)}")

#caso base - condicion que detiene la recursion. Sin el la función se 
#se llamaria infinitamente.
#Caso recursivo = Donde la función se llama a si misma con un 
#problema más pequeño, acercandose al caso base.

def factorial_recursivo(n):
    if n == 0 or n == 1: #Caso base
        return 1
    else:
        return n * factorial_recursivo (n-1)
print(f"Factorial recursivo de 5: {factorial_recursivo(5)}")

#caracteristicas de los procesos recursivos
#Pila de ñllamada (Call Stack

def factorial_visual (n, nivel=0):
    sangria = " " * nivel
    print(f"{sangria} ->  Entrando con n={n}")

    if n == 0 or n == 1:
        print(f"{sangria} <- Caso base, regresa 1")
        return 1
    else:
        resultado = n * factorial_visual( n - 1, nivel + 1)
        print(f"{sangria} <- Regresa {resultado} (n={n})")
        return resultado
    
factorial_visual(4)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci (n - 2)

for i in range(10):
    print(f"Fibonacci {i} = {fibonacci(i)}")

    
