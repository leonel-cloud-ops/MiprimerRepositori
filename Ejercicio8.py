def menu_principal():
    print("\n--- MENÚ DE TRANSFORMACIÓN ---")
    texto = input("Ingrese el texto a transformar: ")
    print("1. Convertir a MAYÚSCULAS")
    print("2. Convertir a minúsculas")
    print("3. Primera letra en Mayúscula")

    try:
        opcion = int(input("Seleccione una opción (1-3): "))
        if opcion in [1, 2, 3]:
            # Usamos la función del Ejercicio 1
            final = "transformar_texto"(texto, opcion)
            print(f"\n>>> Resultado final: {final}")
        else:
            print("Error: Opción fuera de rango.")
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
