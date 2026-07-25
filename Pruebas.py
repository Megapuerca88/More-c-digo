# ==========================================
# VARIABLES GLOBALES
# ==========================================
sesion_iniciada = False #Usamos false para indicar que la sesión no ha sido iniciada al inicio del programa


# ==========================================
# FUNCIONES DE APOYO / ARCHIVOS
# ==========================================

def limpiar_pantalla():
    print("\n" * 30)

def iniciar_sesion():
    global sesion_iniciada
    print("\n--- PANTALLA DE INICIO DE SESIÓN ---")
    usuario = input("Introduce tu usuario: ")
    contrasena = input("Introduce tu contraseña: ")
    
    if usuario == "Carl" and contrasena == "1234":
        print("\n[✓] ¡Bienvenido al sistema, Carl!")
        sesion_iniciada = True #Da la orden de que la sesión ha sido iniciada correctamente
    else:
        print("\n[X] ERROR: Usuario o contraseña incorrectos.") #Si la palbra es erronea sale
        sesion_iniciada = False
        
    input("Presiona Enter para continuar...") #Validacion si se hizo bien


# ==========================================
# MÓDULO: RESUMEN DEL SISTEMA 
# ==========================================

def ver_resumen_sistema():
    print("\n=========================================")
    print("           RESUMEN DEL SISTEMA           ")
    print("=========================================")
    
    print("\n--- PERSONAS SANCIONADAS ---")
    with open("vetados.txt", "a+", encoding="utf8") as archivo: #Con esto se guarda el archivo
        archivo.seek(0) #Y no se borra el contenido al cerrar el programa
        contenido_vetados = archivo.read()
        if contenido_vetados.strip() == "":
            print("Por ahora no hay personas vetadas.")
        else:
            print(contenido_vetados)
            
    print("\n--- LIBROS PRESTADOS ---")
    with open("prestamos.txt", "a+", encoding="utf8") as archivo:
        archivo.seek(0)
        contenido_prestamos = archivo.read()
        if contenido_prestamos.strip() == "":
            print("• 'Sin libros prestados en el registro'")
        else:
            print(contenido_prestamos)
            
    print("=========================================")
    input("\nPresiona Enter para regresar al menú...")


# ==========================================
# MÓDULO: PERSONAS VETADAS
# ==========================================

def menu_vetados():
    print("\n=========================================")
    print("        GESTIÓN DE PERSONAS SANCIONADAS      ") #Cambiamos vetados por sancionadas para que sea más entendible
    print("=========================================")
    print(" [1] - Ver lista de sancionados")
    print(" [2] - Agregar persona a la lista (Sancionar)")
    print(" [3] - Quitar persona de la lista (Quitar sanción)")
    print(" [4] - Regresar al menú principal")
    print("=========================================")
    
    sub_opcion = input("Selecciona una opción (1-4): ")

    if sub_opcion == "1":
        print("\n--- PERSONAS SANCIONADAS ---")
        with open("vetados.txt", "a+", encoding="utf8") as archivo:
            archivo.seek(0)
            contenido = archivo.read()
            if contenido.strip() == "":
                print("Por ahora no hay personas sancionadas.")
            else:
                print(contenido)
        input("\nPresiona Enter para continuar...")

    elif sub_opcion == "2":
        print("\n--- SANCIONAR PERSONA ---")
        nombre = input("Ingresa el nombre a sancionar: ")
        motivo = input("Ingresa el motivo de la sanción: ")
        
        if nombre.strip() != "" and motivo.strip() != "":
            with open("vetados.txt", "a", encoding="utf8") as archivo:
                # Guardamos el nombre junto con el motivo
                archivo.write(f"• {nombre} - Motivo: {motivo}\n")
            print(f"\n[✓] {nombre} ha sido agregado a los sancionados con su motivo.")
        else:
            print("\n[!] El nombre y el motivo no pueden estar vacíos.")
        input("\nPresiona Enter para continuar...")

    elif sub_opcion == "3":
        print("\n--- QUITAR SANCIÓN A LA PERSONA ---")
        nombre_quitar = input("Ingresa el nombre para retirar de la lista de sancionados: ")
        
        try:
            with open("vetados.txt", "r", encoding="utf8") as archivo: 
                lineas = archivo.readlines()
            
            encontrado = False
            with open("vetados.txt", "w", encoding="utf8") as archivo:
                for linea in lineas:
                    # Comprobamos si el nombre ingresado está dentro de la línea
                    if nombre_quitar.strip().lower() not in linea.strip().lower():
                        archivo.write(linea)
                    else:
                        encontrado = True

            if encontrado:
                print(f"\n[✓] {nombre_quitar} ha sido retirado de la lista.")
            else:
                print(f"\n[!] No se encontró a '{nombre_quitar}'.")
        except FileNotFoundError:
            print("\n[!] Aún no existe la lista de sancionados.")
            
        input("\nPresiona Enter para continuar...")


# ==========================================
# MÓDULO: LIBROS PRESTADOS
# ==========================================

def menu_libros():
    print("\n=========================================")
    print("       GESTIÓN DE LIBROS PRESTADOS       ")
    print("=========================================")
    print(" [1] - Ver libros prestados")
    print(" [2] - Registrar nuevo préstamo")
    print(" [3] - Regresar al menú principal")
    print("=========================================")
    
    sub_opcion = input("Selecciona una opción (1-3): ")

    if sub_opcion == "1":
        print("\n--- LIBROS PRESTADOS ---")
        with open("prestamos.txt", "a+", encoding="utf8") as archivo:
            archivo.seek(0)
            contenido = archivo.read()
            if contenido.strip() == "":
                print("• 'Sin libros prestados en el registro'")
            else:
                print(contenido)
        input("\nPresiona Enter para continuar...")

    elif sub_opcion == "2":
        print("\n--- REGISTRAR PRESTAMO ---")
        libro = input("Nombre del libro: ")
        persona = input("Prestado a: ")
        
        if libro.strip() != "" and persona.strip() != "":
            with open("prestamos.txt", "a", encoding="utf8") as archivo:
                archivo.write(f"• '{libro}' - Prestado a: {persona}\n")
            print("\n[✓] Préstamo registrado con éxito.")
        else:
            print("\n[!] Datos incompletos.")
        input("\nPresiona Enter para continuar...")


# ==========================================
# PROCESO PRINCIPAL DEL MENÚ
# ==========================================

def ejecutar_menu():
    global sesion_iniciada
    continuar = True

    while continuar:
        limpiar_pantalla()
        
        # --- MENÚ DE ACCESO (ANTES DE INICIAR SESIÓN) ---
        if not sesion_iniciada:
            print("=========================================")
            print("       SISTEMA DE GESTIÓN BIBLIOTECA     ")
            print("=========================================")
            print(" [1] - Iniciar Sesión")
            print(" [2] - Salir del Sistema")
            print("=========================================")
            
            opcion = input("Selecciona una opción (1-2): ")

            if opcion == "1":
                iniciar_sesion()
            elif opcion == "2":
                print("\nGracias por entrar a la Virtualteca, ¡hasta luego!")
                continuar = False
            else:
                print("\n[!] Opción no válida. Por favor, elige 1 o 2.")
                input("Presiona Enter para reintentar...")

        # --- MENÚ PRINCIPAL COMPLETO (SESIÓN INICIADA) ---
        else:
            print("=========================================")
            print("       SISTEMA DE GESTIÓN BIBLIOTECA     ")
            print("=========================================")
            print(" [1] - Personas Sancionadas")
            print(" [2] - Libros Prestados")
            print(" [3] - Ver Resumen del Sistema")
            print(" [4] - Cerrar Sesión")
            print(" [5] - Salir del Sistema")
            print("=========================================")
            
            opcion = input("Selecciona una opción (1-5): ")

            if opcion == "1":
                menu_vetados()
            elif opcion == "2":
                menu_libros()
            elif opcion == "3":
                ver_resumen_sistema()
            elif opcion == "4":
                sesion_iniciada = False
                print("\n[✓] Sesión cerrada correctamente.")
                input("Presiona Enter para continuar...")
            elif opcion == "5":
                print("\nGracias por entrar a la Virtualteca, ¡hasta luego!")
                continuar = False
            else:
                print("\n[!] Opción no válida. Por favor, elige un número del 1 al 5.")
                input("Presiona Enter para reintentar...")

# Arrancamos el programa
ejecutar_menu()