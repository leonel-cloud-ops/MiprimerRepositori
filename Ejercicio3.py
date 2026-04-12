def procesar_entrada_usuario():
    usuario_texto = input("Ingrese un texto: ")
    usuario_opcion = int(input("Ingrese opción (1: Mayús, 2: Minús, 3: Capitalizar): "))
    print("Resultado:", "transformar_texto"(usuario_texto, usuario_opcion))
