#¿Ques es un subprograma?
#Un subprograma es un bloque de código independiente, 
#con su propio nombre, que realiza una tarea
#especifica y puede ser invocado (llamado) desde 
#cualquier parte del programa principal, las veces que
#necesite

#Funciones y procedimientos.
#Función: Subprograma que SIEMPRE regresa un valor al
#punto donde fue llamado, usando la sentencia return.
#Se usa cuando necesitas un resultado para seguir
#trabajando con él.

#Procedimiento: Subprograma que realiza una acción
#mostrara algo, modificar datos, guardar información),
#pero no necesariamente regresa un valor utilizable.
#se usa cuando el objetivo es ejecutar una tarea, no
#obtener un dato de vuelta.

#def 
#public static int sumar(int a, int b){return a +b}


#EJERCICIO 1: Función vs procedimiento
# 
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area #Regresa un valor es función
   
def mostrar_resultado(nombre, area):
    print(f"El area de {nombre} es {area}m2")
#no regresa un valor es procedimiento

#Uso de ambos subprogramas
resultado = calcular_area_rectangulo(5,5)
mostrar_resultado("El terreno", resultado)

#corregido Saludo buenos dias
def saludar(nombre):
    saludo_base = "Hola buen día"
    return f"{saludo_base} {nombre}"

if __name__ == "__main__":
    c = input("Escribe tu nombre: ")
    mensaje_final = saludar(c)
    print(mensaje_final)

################################
def saludar(saludo, nombre):
   saludo = "Hola buen día "
   c = input("Escribe tu nombre: ")
   nombre = c   
   print(f"{saludo} {nombre:.2f} ")

#El error de no usar return corregir y subir en un nuevo repositorio

def calcular_doble(numero):
    doble = numero * 2
    print(doble)
resultado = calcular_doble(10)
print(resultado)

#Tu turno: Corrige el Ejercicio 2 para que 
# calcular_doble regrese el valor correctamente con return,
#  y que sea el print(resultado) el que se encargue de mostrarlo.

def calcular_doble(numero):
    doble = numero * 2
    return doble

resultado = calcular_doble(15)
print(resultado)