#Sintaxis de funcion

#Encabezado = def nombre_funcion(parametros): - define 
#el nombre y que recibe.

#cuerpo de la funcion - las lineas sw código indentadas que
#wjwcutan la l'ogica de la función.

#Parámetros - los datos que la función recibe para 
#trabajo (pueden ser cero, uno o varios)

#Retorno - la setencia return valor que entrega el resultado de vuelta.

def calcular_promedio(nota1, nota2, nota3): 
    #Encabezado de mi funcuión
    suma = nota1 + nota2 + nota3 #Cuerpo
    promedio = suma / 3
    return promedio # Retorno

resultado = calcular_promedio(8.0, 9.0, 7.0)
print(f"Promedio: {resultado:.2f}") 

#Tu turno: Modifica la funcion para que reciba 4 calificaciones en lugar de 3 
#y ajusta el promedio correctamente

def calcular_promedio(nota1, nota2, nota3, nota4): 
    #Encabezado de mi funcuión
    suma = nota1 + nota2 + nota3 + nota4 #Cuerpo
    promedio = suma / 4
    return promedio # Retorno

resultado = calcular_promedio(8.0, 9.0, 7.0, 5.0)
print(f"Promedio: {resultado:.2f}") 

def mostrar_bienvenida():
    print("==== Sistema de calificaciones ====") #Sin parámetros

def calcular_iva(precio, tasa = 0.16):
    return precio * (1 + tasa)

mostrar_bienvenida()

total1 = calcular_iva(100)
print(f"Total con Iva por defecto: ${total1:.2f}") #Usando valor 
#por defecto de tasa

total2 = calcular_iva(100, 0.08)
print(f"Total con IVA especial: ${total2:.2f}")

#Tu turno: Escribe una función calcular_descuento(precio, porcentaje=10)
#que calcule el precio final con descuento. Pruébala
#una vez sin especificar el porcentaje y otra vez con un porcentaje distinto.

def calcular_descuento(precio2, descuento = 0.10):
    return precio2 * (1 - descuento)

total3 = calcular_descuento(100)
print(f"Total con descuento por defecto: ${total3:.2f}") #Usando valor 
#por defecto de tasa

def calcular_descuento2(precio3, descuentoX = 0.15):
    return precio3 * (1 - descuentoX)
total2 = calcular_descuento(100, 0.15)
print(f"Total con descuento: ${total2:.2f}")

