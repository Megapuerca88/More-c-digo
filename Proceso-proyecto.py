# ==========================================
# MEMORIA GLOBAL DEL SISTEMA
# ==========================================
personas_vetadas = ["Juan Pérez - Motivo: Daño a material de lectura."]
libros_prestados = ["'El Principito' - Prestado a: Sofía Rodríguez"]
historial_dia = []

# VARIABLE DE CONTROL DE SEGURIDAD
# Uso de False
sesion_iniciada = False

# ==========================================
# SECCIÓN DE MÓDULOS / FUNCIONES 
# ==========================================

def iniciar_sesion():
    global sesion_iniciada # Global variable para modificascion general
    
    print("")
    print("--- PANTALLA DE INICIO DE SESIÓN ---")
    usuario = input("Introduce tu usuario: ")
    contrasena = input("Introduce tu contraseña: ")
    
    if usuario == "Carl" and contrasena == "1234":
        print("")
        print("[✓] ¡Bienvenido al sistema, Carl!")
        sesion_iniciada = True # ¡Validado! Se abre el acceso al sistema
        historial_dia.append(f"El usuario '{usuario}' inició sesión correctamente.")
    else:
        print("")
        print("[X] ERROR: Usuario o contraseña incorrectos. Inténtalo de nuevo.")
        historial_dia.append(f"Intento de inicio de sesión fallido con el usuario '{usuario}'.")
    
    input("Presiona Enter para continuar...")

def gestionar_personas_vetadas():
    print("")
    print("--- SECCIÓN DE PERSONAS VETADAS ---")
    print("[1] Ver lista actual")
    print("[2] Vetar a una nueva persona")
    sub_opcion = input("Selecciona una acción (1-2): ")

    if sub_opcion == "1":
        print("\n-- Lista de Vetados --")
        if len(personas_vetadas) == 0:
            print("Por ahora no hay personas vetadas.")
        else:
            for persona in personas_vetadas:
                print(f"• {persona}")
        historial_dia.append("Se consultó la lista de personas vetadas.")

    elif sub_opcion == "2":
        print("\n-- Registrar Nuevo Veto --")
        nombre = input("Nombre de la persona: ")
        motivo = input("Motivo del veto: ")
        
        nuevo_vetado = f"{nombre} - Motivo: {motivo}."
        personas_vetadas.append(nuevo_vetado)
        
        print(f"\n[✓] {nombre} ha sido agregado a la lista de vetados.")
        historial_dia.append(f"Se vetó a: {nombre}.")
    else:
        print("\n[!] Opción incorrecta.")
        
    print("")
    input("Presiona Enter para regresar al menú...")

def gestionar_libros_prestados():
    print("")
    print("--- SECCIÓN DE LIBROS PRESTADOS ---")
    print("[1] Ver libros prestados")
    print("[2] Registrar nuevo préstamo")
    sub_opcion = input("Selecciona una acción (1-2): ")

    if sub_opcion == "1":
        print("\n-- Registro de Préstamos --")
        if len(libros_prestados) == 0:
            print("No hay libros prestados en el registro.")
        else:
            for libro in libros_prestados:
                print(f"• {libro}")
        historial_dia.append("Se consultó la lista de libros prestados.")

    elif sub_opcion == "2":
        print("\n-- Registrar Nuevo Préstamo --")
        titulo = input("Título del libro: ")
        usuario_prestamo = input("¿A quién se le presta?: ")
        
        nuevo_prestamo = f"'{titulo}' - Prestado a: {usuario_prestamo}"
        libros_prestados.append(nuevo_prestamo)
        
        print(f"\n[✓] Préstamo de '{titulo}' registrado con éxito.")
        historial_dia.append(f"Se prestó el libro '{titulo}' a {usuario_prestamo}.")
    else:
        print("\n[!] Opción incorrecta.")

    print("")
    input("Presiona Enter para regresar al menú...")

def ver_resumen_hoy():
    print("")
    print("--- RESUMEN DE HOY ---")
    if len(historial_dia) == 0:
        print("No se ha registrado ninguna actividad el día de hoy.")
    else:
        print("Actividades registradas:")
        for accion in historial_dia:
            print(f"- {accion}")
            
    print("")
    input("Presiona Enter para regresar al menú...")

def limpiar_pantalla():
    print("\n" * 30)


# ==========================================
# PROCESO PRINCIPAL DEL MENÚ
# ==========================================

def ejecutar_menu():
    continuar = True

    while continuar:
        limpiar_pantalla()
        print("=========================================")
        print("       SISTEMA DE GESTIÓN BIBLIOTECA     ")
        print("=========================================")
        print(" [1] - Iniciar Sesión ")
        print(" [2] - Gestionar Personas Vetadas")
        print(" [3] - Gestionar Libros Prestados")
        print(" [4] - Ver Resumen de Hoy (Bitácora)")
        print(" [5] - Salir del Sistema")
        print("=========================================")
        
        # Muestra si inicio sesion o no
        if sesion_iniciada:
            print(" Estado: [✓] Conectado como Carl")
        else:
            print(" Estado: [X] No has iniciado sesión")
        print("=========================================")
        
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            iniciar_sesion()
            
        # Para las opciones 2, 3 y 4 validamos primero si tiene permiso
        elif opcion == "2":
            if sesion_iniciada:
                gestionar_personas_vetadas()
            else:
                print("\n[X] ERROR: Acceso denegado. Debes iniciar sesión primero (Opción 1).")
                input("Presiona Enter para continuar...")
                
        elif opcion == "3":
            if sesion_iniciada:
                gestionar_libros_prestados()
            else:
                print("\n[X] ERROR: Acceso denegado. Debes iniciar sesión primero (Opción 1).")
                input("Presiona Enter para continuar...")
                
        elif opcion == "4":
            if sesion_iniciada:
                ver_resumen_hoy()
            else:
                print("\n[X] ERROR: Acceso denegado. Debes iniciar sesión primero (Opción 1).")
                input("Presiona Enter para continuar...")
                
        elif opcion == "5":
            print("")
            print("Gracias por entrar a la Virtualteca ¡hasta luego!")
            continuar = False  
        else:
            print("")
            print("[!] Opción no válida. Por favor, elige un número del 1 al 5.")
            input("Presiona Enter para reintentar...")

ejecutar_menu()
